function nextStep() {
    let name = document.getElementById("name").value;
    let mobile = document.getElementById("mobile").value;
    let email = document.getElementById("email").value;

    if (!name || !mobile || !email) {
        alert("Please fill all fields");
        return;
    }

    document.getElementById("step1").classList.remove("active");
    document.getElementById("step2").classList.add("active");
}

// BMI CALCULATION + SUGGESTION
document.getElementById("weight").addEventListener("input", calculateBMI);
document.getElementById("height").addEventListener("input", calculateBMI);

function calculateBMI() {
    let w = parseFloat(document.getElementById("weight").value);
    let h = parseFloat(document.getElementById("height").value);

    if (w > 0 && h > 0) {
        let bmi = (w / ((h / 100) ** 2)).toFixed(1);
        document.getElementById("bmi").value = bmi;
        generateSuggestion(bmi);
    }
}

function generateSuggestion(bmi) {
    let suggestion = "";

    if (bmi < 18.5) suggestion = "Underweight → Recommended: Weight Gain";
    else if (bmi < 25) suggestion = "Normal → Maintain or Build Aesthetic Physique";
    else if (bmi < 30) suggestion = "Overweight → Recommended: Weight Loss";
    else suggestion = "Obese → Strongly Recommended: Weight Loss";

    document.getElementById("suggestion").value = suggestion;
}

function finish() {
    alert("Registration Successful!");
}
