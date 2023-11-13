# This import script runs the main() function on bad_script by accident
# import bad_script

# Since scipt_temlpate does include an if statement checking if it's
# __main__ therefore code is not ran.
import script_template

# if we do want to run the main method in script_template, we call it explicitly
script_template.main()
