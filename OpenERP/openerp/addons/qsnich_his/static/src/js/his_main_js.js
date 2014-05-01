openerp.qsnich_his = function(instance){

	console.log("Yo------------------");

	openerp.qsnich_his.his_patient(instance);
	openerp.qsnich_his.his_message(instance);
	openerp.qsnich_his.his_regis(instance);


	instance.web.client_actions.add('qsnich_his.MenuAction', 'instance.qsnich_his.his_patient.MenuAction_function');
	instance.web.client_actions.add('qsnich_his.MessgeAction', 'instance.qsnich_his.his_message.MessageAction_function');

};
