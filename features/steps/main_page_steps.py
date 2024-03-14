from behave import given, when, then


@when('I Click on “off plan” button')
def click_menu_block_button(context, button):
    context.app.main_page.click_menu_block_button(button)

@then('Verify the right page opens')
def verify_main_page(context):
    context.app.main_page.verify_main_page()