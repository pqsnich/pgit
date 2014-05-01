# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

import time

class Patient(osv.Model):
    _name = 'his_code.patient'
#    _rec_name = 'full_name'
    _rec_name = 'first_name'
    
    def _get_full_name(self, cr, uid, ids, field_name, arg, context):
        name_title = {'Boy':'เด็กชาย','Girl':'เด็กหญิง','Mr.':'นาย','Ms.':'นางสาว','Mrs.':'นาง'}
    
        patients = self.browse(cr, uid, ids)
        result = {}
        for p in patients:
            result[p.id] = ('%s %s %s' % (name_title[p.title], p.first_name, p.last_name))
        return  result  
    
    _columns = {
        'title': fields.selection([('Boy','เด็กชาย'),('Girl','เด็กหญิง'),('Mr.','นาย'),('Ms.','นางสาว'),('Mrs.','นาง')], string='คำนำหน้าชื่อ', required=True),        
        'first_name': fields.char('ชื่อ',size=256,  required=True),    
        'last_name': fields.char('นามสกุล', size=256, required=True),
        'sex': fields.selection([('M','ชาย'),('F','หญิง')], string='เพศ', required=True),        
        'id_number': fields.char('เลขบัตรประชาชน', size=20, required=True),
        'full_name': fields.function(_get_full_name, type='char'), 
        'appointment_ids': fields.one2many('his_code.appointment','patient_id','ประวัติการนัดพบแพทย์'), 
    }

class Message(osv.Model):
    _name = 'his_code.message' 
    _columns = {
        'message': fields.char('ข้อความ', size=50, required=True),
    }

class Appointment(osv.Model):
    _name = 'his_code.appointment'
    
    _rec_name = 'appointment_date'

    _columns = {
        'appointment_date': fields.date(string='วันนัดหมาย',required=True),
        'patient_id': fields.many2one('his_code.patient','ชื่อผู้ป่วย'),
        'clinic_name': fields.many2one('his_code.department','คลินิก'),
        'state':fields.selection([
                ('make_appointment','นัดพบแพทย์'),
                ('walk_in','มาพบแพทย์แบบไม่นัด'),
                ('arrived','มาพบแพทย์ตามนัด'),
                ('examining','Examining by Physician'),
                ('wait_medicine','Awaiting Medicine'),
                ('done','Done'),
                ('cancel','Cancel'),
                ],
                'Status', readonly=True),
    }

class Department(osv.Model):
    _name = 'his_code.department'

    def _filter_today_appointment(self,cr ,uid ,ids ,field_name=None,arg=None,context=None):
        dsearches = self.browse(cr, uid, ids)
        
        appointment_obj = self.pool.get('his_code.appointment')

        now = time.strftime("%c")
        print "Current date " + now
        
        result = {}
        for dsearch in dsearches:
            result[dsearch.id] = (appointment_obj.search(cr,uid,
                                                        [('clinic_name','=',dsearch.name),
                                                         ('appointment_date','>=', now)
                                                        ],
                                                        context = context))
            
        return  result
    
    _columns = {
        'name': fields.char(string='คลินิก', size=200, required=True),
        'appointment_id' : fields.function(_filter_today_appointment,type = 'one2many',
                                           relation='his_code.appointment',string='Today Appointments'),
#        'appointment_id': fields.one2many('his_code.appointment','clinic_name','Appointments'),
    }

class DepartmentSearch(osv.TransientModel):
    _name = 'his_code.departmentsearch' 
    
    def appointment_search(self,cr ,uid ,ids ,field_name=None,arg=None,context=None):
        dsearches = self.browse(cr, uid, ids)
        
        appointment_obj = self.pool.get('his_code.appointment')
        
        result = {}
        for dsearch in dsearches:
            result[dsearch.id] = (appointment_obj.search(cr,uid,
                                                        [('clinic_name','=',dsearch.clinic_name.id),
                                                         ('appointment_date','=',dsearch.search_date)],
                                                         context = context))
            
        return  result

    _columns = {
        'clinic_name': fields.many2one('his_code.department','Department'),
        'search_date': fields.date(string='วันที่ต้องการหา'),
        'appointment_ids': fields.function(appointment_search,type = 'one2many',
                                           relation='his_code.appointment',string='Appointment by date'),
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: