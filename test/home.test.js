/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const { ToggleMenu } = require("../static/js/script.js");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("home.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});