const fs = require('fs');
const handlebars = require('handlebars');

// Step 1: Load the template file (template.hbs)
let templateSource;
try {
    templateSource = fs.readFileSync('template.hbs', 'utf-8');
} catch (err) {
    console.error('Error reading template.hbs:', err);
    process.exit(1);
}

// Step 2: Compile the template with Handlebars
let template;
try {
    template = handlebars.compile(templateSource);
} catch (err) {
    console.error('Error compiling template:', err);
    process.exit(1);
}

// Step 3: data to be put in the template
const data = {
    firstName: 'John',
    signInTime: 'February 11, 2025 10:00 AM',
    device: 'iPhone 13',
    securityLink: 'https://example.com/change-password'
};

// Step 4: Render the template with data
let result;
try {
    result = template(data);
} catch (err) {
    console.error('Error rendering template:', err);
    process.exit(1);
}

// Step 5: render HTML to the console `
console.log(result);

// write the result to an HTML file:
try {
    fs.writeFileSync('output.html', result);
    console.log('output.html has been created successfully.');
} catch (err) {
    console.error('Error writing to file:', err);
    process.exit(1);
}