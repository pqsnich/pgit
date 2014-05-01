import openerp.addons.web.http as http
import simplejson as json
import urllib2


class MyController(http.Controller):
    _cp_path = '/qsnich_his/ajax'
    
    @http.httprequest
    def index(self, req, s_action=None, **kwargs):
        pid = req.params['pid']
        request_url = "http://theory.cpe.ku.ac.th:8080/%s" % pid
        contents = urllib2.urlopen(request_url)
        return contents.read()
    