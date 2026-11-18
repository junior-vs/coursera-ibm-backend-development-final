from backend import app

if __name__ == "__main__":  # Script executed directly?
    print("pictures microservice.")
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)

# Run it from the project root with:
# python app.py
