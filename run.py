from market import app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)

# for item in Item.query.all():
#     item.name
#     item.price
#     item.description
#     item.id
#     item.barcode
# for item in Item.query.filter_by(price=500):
#     item.name
