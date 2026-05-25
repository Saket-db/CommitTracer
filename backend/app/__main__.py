from backend.app import create_app


def main() -> None:
    """Run the Flask app when the package is executed with -m."""
    create_app().run(debug=True)


if __name__ == "__main__":
    main()
