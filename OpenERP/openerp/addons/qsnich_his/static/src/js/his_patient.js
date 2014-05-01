openerp.qsnich_his.his_patient = function(instance){


	instance.qsnich_his.his_patient = {};
	instance.qsnich_his.his_patient.MenuAction_function = instance.web.Widget.extend({
		template: 'qsnich_his.custom_menu',

		events: {
			'click .oe_qsnich_his_patient_new_link': 'link_click',
			'click .oe_qsnich_his_patient_query_link': 'patient_query',
		},

		link_click: function(){
			this.do_action({
		     	type:'ir.actions.act_window',
		  	    res_model: 'his_code.patient',
		  	    views: [[false,'form']],
		  	    target: 'current',
		 	    context: {},
			});
			return true;
		},

		patient_query: function() {
			//alert('patient_query');
			var model = new instance.web.Model('his_code.patient');
			var self = this;
			model.query().all().done(function(results){

				//alert("count="+results.length);
			
				for(var i=0; i <results.length; i++) {
					self.$(".oe_qsnich_his_patient_results").append('<li>' + results[i].first_name + ' ' + results[i].last_name +'</li>');
		        	}
			});
			return true;
		},
	});


};

