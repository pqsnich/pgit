openerp.qsnich_his.his_message = function(instance){

	instance.qsnich_his.his_message = {};
	instance.qsnich_his.his_message.popupInterval = null;
	instance.qsnich_his.his_message.MessageAction_function = instance.web.Widget.extend({

		template: 'qsnich_his.message_service',
		events: {
			'click .oe_qsnich_his_start': 'startCheckingMessage',
			'click .oe_qsnich_his_stop': 'stopCheckingMessage',
		},

		startCheckingMessage: function() {
			var self = this;
			console.log("Start to check a new message...");

			instance.qsnich_his.his_message.popupInterval = setInterval(function() {self.popup();},5000);
			this.shownMsgId = 0;	
	 	},

		stopCheckingMessage: function() {

			alert(instance.qsnich_his.his_message.popupInterval);
			if(instance.qsnich_his.his_message.popupInterval){
			    clearInterval(instance.qsnich_his.his_message.popupInterval);
			}
	 	},


		
		fetchNewMessage: function(recentId, callback) {
			console.log("fetchNewMessage to check a new message...");
			var model = new instance.web.Model('his_code.message');
			var self = this;
			model.query().filter([['id','>',recentId]]).all().done(function(results){
				if (results.length > 0) {
					msgId = results[results.length-1].id;
					callback(msgId);
				}
			});
	 	},

		 popup: function() {
            		var self = this;
            		this.fetchNewMessage(this.shownMsgId, function(msgId) {
                		self.do_action({
                    			type: 'ir.actions.act_window',
                    			res_model: "his_code.message",
                    			res_id: msgId,
                    			views: [[false, 'form']],
                    			target: 'new',
                    			context: {},
                		});
                		self.shownMsgId = msgId;
           		 });
        	}
        });
};
