from calorieApp.calorie_app import CalorieApp
import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "a,r", ["add_admin", "remove_admin"])
    except getopt.GetoptError:
        print('admin_manager.py -a/-r <admin_id> | admin_manager.py --add_admin/--remove_admin <admin_id>')
        sys.exit(2)
    if len(opts) != 1 or len(args) != 1:
        print('admin_manager.py -a/-r <admin_id> | admin_manager.py --add_admin/--remove_admin <admin_id>')
        sys.exit(2)
    app = CalorieApp()

    opt = opts[0]
    admin_id = args[0]

    if '-a' == opt[0] or '--add_admin' == opt[0]:
        app.add_admin(admin_id)
        exit(0)

    if '-r' == opt[0] or '--remove_admin' == opt[0]:
        app.remove_admin(admin_id)
        exit(0)


if __name__ == '__main__':
    main(sys.argv[1:])
