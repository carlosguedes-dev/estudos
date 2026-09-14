# INQUIRER CLI PROMPTS
const inquirer = require('inquirer');
inquirer.prompt([{type: 'input', name: 'name', message: 'Name?'}]).then(answers => console.log(answers));
