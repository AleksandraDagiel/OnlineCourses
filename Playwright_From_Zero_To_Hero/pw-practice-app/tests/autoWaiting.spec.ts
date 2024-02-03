import {expect, test} from '@playwright/test'


test.beforeEach(async ({page}) => {
    await page.goto('http://uitestingplayground.com/ajax')
    await page.getByText('Button triggering AJAX Request').click()
})

test('auto waiting', async ({page}) => {
    const successButton = page.locator('.bg-success')

    await successButton.click()   //you can specify timeout in config

    const text = await successButton.textContent()
    expect(text).toEqual('Data loaded with AJAX get request.')

    await successButton.waitFor({state: 'attached'})
    const textall = await successButton.allTextContents()
    expect(textall).toContain('Data loaded with AJAX get request.')

    await expect(successButton).toHaveText('Data loaded with AJAX get request.', {timeout: 20000})
})

test('alternative waits', async ({page}) => {
    const successButton = page.locator('.bg-success')

    //___ wait for element
    await page.waitForSelector('.bg-success')

    //___ wait for particular response
    await page.waitForResponse('http://uitestingplayground.com/ajaxdata')

    //____wait for network calls to be completed (NOT RECOMMENDED)
    await page.waitForLoadState('networkidle')

    const textall = await successButton.allTextContents()
    expect(textall).toContain('Data loaded with AJAX get request.')
})