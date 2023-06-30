from flask import Flask
from flask_cors import CORS
from routes import Plant, File_Action, PromisedDate
from routes import Style_Customer, Style_GlobalCategory, Style_Workcenter, Style_GeneralInfo, Style_Sewing, Style_Sewing_Family, Style_Sewing_LayoutConfiguration, Style_CustomerService_ProductType, Style_CustomerService_Vendor, Style_CustomerService_LT
from routes import Demand_Cycle, Demand_Forecast, Demand_OnPO, File_ActionForecast
from routes import General_GetTokenPowerBi

app = Flask(__name__)
# Routes
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def index():
    return "<h1>Welcome to our server s!!</h1>"

app.register_blueprint(Plant.main, url_prefix='/api/Plant')
app.register_blueprint(File_Action.main, url_prefix='/api/File')
app.register_blueprint(File_ActionForecast.main, url_prefix='/api/FileForecast')
app.register_blueprint(PromisedDate.main, url_prefix='/api/PromisedDate')
app.register_blueprint(Style_Customer.main, url_prefix='/api/Style_Customer')
app.register_blueprint(Style_GlobalCategory.main, url_prefix='/api/Style_GlobalCategory')
app.register_blueprint(Style_Workcenter.main, url_prefix='/api/Style_Workcenter')
app.register_blueprint(Style_GeneralInfo.main, url_prefix='/api/Style_GeneralInfo')
app.register_blueprint(Style_Sewing.main, url_prefix='/api/Style_Sewing')
app.register_blueprint(Style_Sewing_Family.main, url_prefix='/api/Style_Sewing_Family')
app.register_blueprint(Style_Sewing_LayoutConfiguration.main, url_prefix='/api/Style_Sewing_LayoutConfiguration')
app.register_blueprint(Style_CustomerService_ProductType.main, url_prefix='/api/Style_CustomerService_ProductType')
app.register_blueprint(Style_CustomerService_Vendor.main, url_prefix='/api/Style_CustomerService_Vendor')
app.register_blueprint(Style_CustomerService_LT.main, url_prefix='/api/Style_CustomerService_LT')
app.register_blueprint(Demand_Cycle.main, url_prefix='/api/Demand_Cycle')
app.register_blueprint(Demand_Forecast.main, url_prefix='/api/Demand_Forecast')
app.register_blueprint(Demand_OnPO.main, url_prefix='/api/Demand_OnPO')
app.register_blueprint(General_GetTokenPowerBi.main, url_prefix='/api/General_GetTokenPowerBi')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', threaded=True, port=5000, debug=True, ssl_context=('certfile.crt', 'keyfile.key'))
    # app.run(host='0.0.0.0', threaded=True, port=5000, debug=False, ssl_context=('certificado.crt', 'clave_privada.key'))
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True, ssl_context=('certificado.crt', 'clave_privada.key'))

