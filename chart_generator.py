import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
import base64

matplotlib.use('Agg')

def generate_pie_chart(categories, amounts):
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Expense Analysis')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return img_base64
