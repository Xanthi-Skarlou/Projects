function discriminant(a,b,c) {
    let d;
    let root1, root2;
    if (a==0 || c==0) {
        d = b*b;
    }
    else if (b==0) {
        d = (-4)*a*c;
    }
    else {
        d = ((b**2)-(4*a*c));
    }
    
    if (d>0) {
        root1 = (-b + Math.sqrt(d)) / (2 * a);
        root2 = (-b - Math.sqrt(d)) / (2 * a);
        document.getElementById("result").innerHTML = " Η διακρίνουσα είναι " + d + 
        " με πρώτη λύση τη x1 = " + root1 + " και δεύτερη τη x2 = " + root2;
    }
    else if (d==0) {
        root1 = root2 = -b / (2 * a);
        document.getElementById("result").innerHTML = " Η διακρίνουσα είναι " + d +
        " με διπλή λύση τη x = " + root1;
    }
    else {
        document.getElementById("result").innerHTML = "Δεν υπάρχουν πραγματικές ρίζες";
    }
}

function disc() {
    let a = parseInt(document.getElementById("numberA").value);
    let b = parseInt(document.getElementById("numberB").value);
    let c = parseInt(document.getElementById("numberC").value);
    let result = discriminant(a,b,c);
}