from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from urllib.parse import quote_plus as urlquote
from decimal import Decimal

app = Flask(__name__)
# 处理跨域问题
CORS(app)

HOSTNAME = '10.10.1.38'
PORT = '9030'
DATABASE = 'dwd_u9erp'
USERNAME = 'odata'
PASSWORD = urlquote('odata@starrocks')
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class SaleDetails(db.Model):
    __tablename__ = 'sm_ship_line_dt'
    id = db.Column(db.Integer, nullable=False, autoincrement=True)
    org_id = db.Column(db.Integer, nullable=False)
    doc_type = db.Column(db.String(80), unique=True, nullable=False)
    line_confirm_date = db.Column(db.Date, nullable=False)
    model = db.Column(db.String(80), nullable=False)
    ship_qty_inv_amount = db.Column(db.Float, nullable=False)
    fc_sales_price = db.Column(db.Float, nullable=False)
    total_money_fc = db.Column(db.String(80), nullable=False)
    item_code = db.Column(db.String(80), nullable=False)
    # 使用db.PrimaryKeyConstraint定义联合主键
    __table_args__ = (
        db.PrimaryKeyConstraint('id', 'org_id'),
    )

    def __repr__(self):
        return '<SaleDetails %r>' % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'org_id': self.org_id,
            'doc_type': self.doc_type,
            'line_confirm_date': self.line_confirm_date,
            'model': self.model,
            'ship_qty_inv_amount': self.ship_qty_inv_amount,
            'fc_sales_price': self.fc_sales_price,
            'total_money_fc': round(self.total_money_fc, 2),
            'discount': str((0.06 * 100)) + '%',
            'discount_price': round(self.total_money_fc * Decimal('0.06'), 4),
            'item_code': self.item_code
        }


@app.route('/')
def index():
    return "API is running!"


@app.route('/api/saleDetails', methods=['GET'])
def data():
    where_in = ['66020030000008', '66020030000007', '66010080000027']
    sale_details = SaleDetails.query.filter(
        SaleDetails.item_code.in_(where_in)).order_by(
        SaleDetails.id.desc()).limit(5)
    return jsonify([sale_detail.to_dict() for sale_detail in sale_details])


if __name__ == '__main__':
    app.run(port=8080, debug=True)
