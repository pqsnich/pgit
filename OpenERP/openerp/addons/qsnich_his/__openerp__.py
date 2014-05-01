# -*- coding: utf-8 -*-
{
    'name' : 'ระบบโรงพยาบาล QSNICH',
    'version' : '0.1',
    'author' : 'QSNICH Development Team',
    'category': 'Hospital Information System',
    'description' : "QSNICH Hospital Information System",
    'depends' : [
        'web',
    ],
    'data' : [
        'his_view.xml',
        'his_report.xml',
        'his_workflow.xml',
        
    ],
    'css' : [
        'static/src/css/his_css.css',
    ],
    'js' : [
        'static/src/js/his_main_js.js',
        'static/src/js/his_message.js',
        'static/src/js/his_patient.js',
        'static/src/js/his_regis.js',
    ],
    'qweb' : [
        'static/src/xml/his_qweb.xml',
    ],
    'installable' : True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: