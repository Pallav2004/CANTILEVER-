from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    df = pd.read_excel("products.xlsx")
    query = request.args.get("q", "")
    rating_filter = request.args.get("rating", "")
    
    # Filter by search query
    if query:
        df = df[df['Title'].str.contains(query, case=False)]
    
    # Filter by rating if selected
    if rating_filter:
        df = df[df['Rating'] == rating_filter]
    
    products = df.to_dict(orient='records')
    
    # Unique ratings to populate filter dropdown
    ratings = sorted(df['Rating'].unique())
    
    return render_template("index.html", products=products, query=query, rating_filter=rating_filter, ratings=ratings)

if __name__ == "__main__":
    app.run(debug=True)

