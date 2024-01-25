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