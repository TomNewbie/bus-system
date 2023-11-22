const { By, Builder, until } = require("selenium-webdriver");

(async function helloSelenium() {
  let driver;

  try {
    driver = await new Builder().forBrowser("chrome").build();
    // Open list of busses
    await driver.get("http://127.0.0.1:5173/");
    console.log("Open list of busses");
    await delay(2000);

    // Choose one bus
    let busLineButton = await driver.wait(
      until.elementLocated(By.css(".bus-1600286")),
      500000 // Adjust the timeout as needed (in milliseconds)
    );
    await delay(2000);

    await driver.wait(until.elementIsVisible(busLineButton), 100);
    await busLineButton.click();
    console.log("Choose one bus");
    await delay(2000);

    // Choose one stop

    //Exit bus line popover
    let exitLineButton = await driver.wait(
      until.elementLocated(By.css(".exit-button-busline")),
      500000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(exitLineButton), 100);
    await exitLineButton.click();
    console.log("Exit bus line popover");
    await delay(2000);

    //Exit bus list popover
    let exitButton = await driver.wait(
      until.elementLocated(By.css(".exit-button")),
      500000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(exitButton), 100);
    await exitButton.click();
    console.log("Exit bus list popover");
    await delay(2000);
    // List bus line
    let openButton = await driver.wait(
      until.elementLocated(By.css(".open-button")),
      500000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(openButton), 100);
    await openButton.click();
    console.log("Open list of busses");
    await delay(2000);
  } catch (error) {
    console.error("An error occurred:", error);
  } finally {
    await driver.quit();
  }
})();

// Function to create a delay using Promises
function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
