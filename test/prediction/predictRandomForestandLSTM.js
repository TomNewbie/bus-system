const { By, Builder, until } = require("selenium-webdriver");

(async function helloSelenium() {
  let driver;

  try {
    driver = await new Builder().forBrowser("edge").build();
    // Open list of busses
    await driver.get("http://127.0.0.1:5173/");
    console.log("Open list of busses");
    await delay(5000);

    // Choose one bus
    let busLineButton = await driver.wait(
      until.elementLocated(By.css(".bus-1600286")),
      500000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(busLineButton), 100);
    await delay(5000);
    await busLineButton.click();
    console.log("Choose one bus");
    await delay(5000);

    //Enable prediction
    //Choose LSTM
    let enableButton = await driver.wait(
      until.elementLocated(By.css(".enable-button")),
      500000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(enableButton), 1000);
    await enableButton.click();
    console.log("Choose LSTM");
    await delay(500);

    // // Click on the button to open the dropdown
    // let dropdownButton = await driver.wait(
    //   until.elementLocated(By.css(".dropdown")),
    //   500000 // Adjust the timeout as needed (in milliseconds)
    // );

    // await driver.wait(until.elementIsVisible(dropdownButton), 1000);
    // await dropdownButton.click();
    // console.log("Click dropdown");
    // await delay(500);

    // // Find all elements representing the items in the dropdown
    // const dropdownItems = await driver.findElements(By.css(".dropdown-item"));

    // //10 minutes

    // await dropdownItems[1].click();
    // console.log("Click ", 1);
    // await delay(5000);
    // //20 minutes
    // await dropdownButton.click();
    // await dropdownItems[2].click();
    // console.log("Click ", 2);
    // await delay(5000);
    // //30 minuts
    // await dropdownButton.click();
    // await dropdownItems[3].click();
    // console.log("Click ", 3);
    // await delay(5000);

    //Choose Random Forest
    let randomForestButton = await driver.wait(
      until.elementLocated(By.css(".random-forest")),
      5000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(randomForestButton), 1000);
    await randomForestButton.click();
    //10 minutes
    let dropdownButton1 = await driver.wait(
      until.elementLocated(By.css(".dropdown")),
      5000 // Adjust the timeout as needed (in milliseconds)
    );

    await driver.wait(until.elementIsVisible(dropdownButton1), 1000);
    await dropdownButton1.click();
    console.log("Click dropdown");
    await delay(500);

    // Find all elements representing the items in the dropdown
    const dropdownItems1 = await driver.findElements(By.css(".dropdown-item"));
    await dropdownItems1[1].click();
    console.log("Click ", 1);
    await delay(10000);
    //20 minutes
    await dropdownButton1.click();
    await dropdownItems1[2].click();
    console.log("Click ", 2);
    await delay(10000);
    //30 minuts
    await dropdownButton1.click();
    await dropdownItems1[3].click();
    console.log("Click ", 3);
    await delay(5000);
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
