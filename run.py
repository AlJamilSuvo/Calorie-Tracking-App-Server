from calorieApp.calorie_app import CalorieApp


def main():
    app = CalorieApp()
    app.run(host='0.0.0.0', port=2121)


if __name__ == '__main__':
    main()
