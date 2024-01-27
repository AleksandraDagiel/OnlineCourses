import {test} from '@playwright/test'

test.beforeEach(async ({page}) => {
    await page.goto('http://localhost:4200/')
})

test.describe('suite1', () => {
    test.beforeEach(async ({page}) => {
        await page.getByText('Forms').click()
    })

    test('the first test', async ({page}) => {
        await page.getByText('Form Layouts').click()
    })
    
    test('second test', async ({page}) => {
        await page.getByText('Datepicker').click()
    })
})

test.describe('suite2', () => {
    test.beforeEach(async ({page}) => {
        await page.getByText('Modal & Overlays').click()
    })

    test('third test', async ({page}) => {
        await page.getByText('Dialog').click()
    })
    
    test('fourth test', async ({page}) => {
        await page.getByText('Window').click()
    })
})

test.describe.skip('suite3', () => {
    test.beforeEach(async ({page}) => {
        await page.getByText('Charts').click()
    })

    test('fifth test', async ({page}) => {
        await page.getByText('Echarts').click()
    })
})

test.afterEach(async ({page}) => {
    page.close()
})

test('Locator syntax rules', async({page}) => {
    //by Tag name
    page.locator('input')

    //by ID
    page.locator('#inputEmail1')

    //by Class value
    page.locator('.shape-rectangle')

    //by attribute
    page.locator('[placeholder="Email"')

    //by Class value (full)
    page.locator('[class="input-full-width size-medium status-basic shape-rectangle nb-transition"')

    //combine different selectors
    page.locator('input[placeholder="Email"][nbinput]')

    //by XPath (NOT RECOMMENDED
    page.locator('//*[@id="inputEmail')

    //by partial text match
    page.locator('.text("Using")')

    //bt exact text match
    page.locator(':text-is("Using the Grid')
})

test.describe("Geting locator that are visible by user", () => {
    test.beforeEach(async ({page}) => {
        await page.getByText('Forms').click()
        await page.getByText('Form Layouts').click()
    })

    test('User facing locators', async({page}) => {
        await page.getByText('Forms').click()
        
        await page.getByText('Form Layouts').click()
        
        await page.getByRole('textbox', {name: "Email"}).first().click()
        
        await page.getByRole('button',{name: 'Sign in'}).first().click()
    
        await page.getByLabel('Email').first().click()
    
        await page.getByPlaceholder('Jane Doe').click()
    
        await page.getByText('Using The Grid').click()

        await page.getByTitle('IoT Dashboard').click()

        // await page.getByTestId('SomeName').click()  -> you need to add data-testid="SomeName" to the source code of the app
    })

    test('Locating child elements', async({page}) => {
        await page.locator('nb-card nb-radio :text-is("Option 1")').click()
        await page.locator('nb-card').locator('nb-radio').locator(':text-is("Option 2")').click()
    
        await page.locator('nb-card').getByRole('button', {name: "Sign in"}).first().click()

        await page.locator('nb-card').nth(3).getByRole('button').click()  // index from 0
    })

    test('locating parent elements', async({page}) => {
        await page.locator('nb-card', {hasText: 'Using the Grid'}).getByRole('textbox', {name: "Email"}).click()
        await page.locator('nb-card', {has: page.locator('#inputEmail1')}).getByRole('textbox', {name: "Email"}).click()

        await page.locator('nb-card').filter({hasText: "Basic form"}).getByRole('textbox', {name: "Email"}).click()
        await page.locator('nb-card').filter({has: page.locator('.status-danger')}).getByRole('textbox', {name: "Password"}).click()

        await page.locator('nb-card').filter({has: page.locator('nb-checkbox')}).filter({hasText: "Sign in"})
            .getByRole('textbox', {name: "Email"}).click()

        //not recommended by xpath:
        await page.locator(':text-is("Using the Grid")').locator('..').getByRole('textbox', {name: "Email"}).click()
    })
})


