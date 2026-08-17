from flask import Flask
app = Flask(__name__)
@app.route('/')
def bill():
    products = [
        ("Laptop", 1, 45000),
        ("Mouse", 2, 500),
        ("Keyboard", 1, 1200),
        ("Pendrive", 3, 600),
        ("Headphones", 1, 2000)
    ]
    total = 0
    html = """
    <h1>Product Bill</h1>
    <table border="1" cellpadding="8">
    <tr>
        <th>Product</th>
        <th>Quantity</th>
        <th>Price</th>
        <th>Amount</th>
    </tr>
    """
    for name, qty, price in products:
        amount = qty * price
        total += amount
        html += f"""
        <tr>
            <td>{name}</td>
            <td>{qty}</td>
            <td>₹{price}</td>
            <td>₹{amount}</td>
        </tr>
        """
    if total > 5000:
        discount = total * 0.10
    else:
         discount = 0
    subtotal = total - discount
    gst = subtotal * 0.18
    final_bill = subtotal + gst
    html += f"""
    </table>
    <br>
    <b>Total Bill :</b> ₹{total}<br><br>
    <b>Discount :</b> ₹{discount}<br><br>
    <b>GST (18%) :</b> ₹{gst}<br><br>
    <h2>Final Bill : ₹{final_bill:.2f}</h2>
    """
    return html
if __name__ == "__main__":
     app.run(debug=True)