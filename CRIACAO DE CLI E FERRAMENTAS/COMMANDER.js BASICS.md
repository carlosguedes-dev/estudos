# COMMANDER.js BASICS
const { program } = require('commander');
program.option('-d, --debug').parse(process.argv);
