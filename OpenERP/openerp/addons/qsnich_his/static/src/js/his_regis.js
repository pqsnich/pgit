openerp.qsnich_his.his_regis = function(instance) {
	instance.qsnich_his.regis = {}
	instance.qsnich_his.regis.FieldPID = instance.web.form.FieldChar.extend({
		template: 'qsnich_his.FieldPID',
		events:{
			'click .oe_qsnich_his_pid_search': function(e){
			   var url = "/qsnich_his/ajax?pid="+$(".oe_qsnich_his_pid_search").parent().find("input").val();
			   $.getJSON(url, function(data){
			     $(".oe_qsnich_his_firstname input").val(data.firstname);
			     $(".oe_qsnich_his_lastname input").val(data.lastname);
			   });
		    },	
	    },
  	});
  	instance.qsnich_his.regis.FieldFirstName = instance.web.form.FieldChar.extend({
		template: 'qsnich_his.FieldFirstName',
  	});
  	instance.qsnich_his.regis.FieldLastName = instance.web.form.FieldChar.extend({
		template: 'qsnich_his.FieldLastName',
  	});
  	
	instance.web.form.widgets.add('person_id','instance.qsnich_his.regis.FieldPID');
	instance.web.form.widgets.add('firstname','instance.qsnich_his.regis.FieldFirstName');
	instance.web.form.widgets.add('lastname','instance.qsnich_his.regis.FieldLastName');
};
