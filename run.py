from api import app
import os

if __name__ == "__main__":
    print("Chamando arquivo direto!!")
    app.run(host="0.0.0.0",port=os.environ.get('PORT_FLASK'), debug=True)
