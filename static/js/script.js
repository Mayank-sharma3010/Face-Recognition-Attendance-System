// =====================================
// FACE RECOGNITION ATTENDANCE SYSTEM
// MAIN JAVASCRIPT
// =====================================


// Wait until page is completely loaded

document.addEventListener("DOMContentLoaded", function () {

    console.log(
        "Face Recognition Attendance System Loaded Successfully"
    );

    highlightActiveMenu();

});


// =====================================
// ACTIVE SIDEBAR MENU
// =====================================

function highlightActiveMenu() {

    const links = document.querySelectorAll(".sidebar a");

    const currentPath = window.location.pathname;


    links.forEach(function (link) {

        link.classList.remove("active");


        if (link.getAttribute("href") === currentPath) {

            link.classList.add("active");

        }

    });

}


// =====================================
// START ATTENDANCE
// =====================================

function startAttendance() {

    const confirmStart = confirm(
        "Do you want to start Face Recognition Attendance?"
    );


    if (confirmStart) {

        window.location.href = "/attendance";

    }

}


// =====================================
// REGISTER STUDENT
// =====================================

function registerStudent() {

    window.location.href = "/register";

}


// =====================================
// VIEW ATTENDANCE RECORDS
// =====================================

function viewRecords() {

    window.location.href = "/records";

}


// =====================================
// SHOW SUCCESS MESSAGE
// =====================================

function showSuccessMessage(message) {

    alert(message);

}


// =====================================
// SHOW ERROR MESSAGE
// =====================================

function showErrorMessage(message) {

    alert("Error: " + message);

}


// =====================================
// CONFIRM DELETE STUDENT
// =====================================

function confirmDelete(studentName) {

    return confirm(

        "Are you sure you want to delete " +

        studentName +

        "?"

    );

}


// =====================================
// LIVE DATE AND TIME
// =====================================

function updateDateTime() {

    const dateTimeElement =
        document.getElementById("dateTime");


    if (dateTimeElement) {

        const now = new Date();


        dateTimeElement.innerHTML =

            now.toLocaleDateString()

            +

            " | "

            +

            now.toLocaleTimeString();

    }

}


// Update time every second

setInterval(updateDateTime, 1000);


// Run immediately

updateDateTime();


// =====================================
// ATTENDANCE SEARCH
// =====================================

function searchAttendance() {

    const input =
        document.getElementById("searchInput");


    if (!input) {

        return;

    }


    const filter =
        input.value.toLowerCase();


    const table =
        document.getElementById("attendanceTable");


    if (!table) {

        return;

    }


    const rows =
        table.getElementsByTagName("tr");


    for (

        let i = 1;

        i < rows.length;

        i++

    ) {

        const text =
            rows[i]
                .textContent
                .toLowerCase();


        if (

            text.includes(filter)

        ) {

            rows[i].style.display = "";

        }

        else {

            rows[i].style.display = "none";

        }

    }

}


// =====================================
// CAMERA STATUS
// =====================================

function cameraStarted() {

    console.log(
        "Face Recognition Camera Started"
    );


    showSuccessMessage(

        "Camera started successfully."

    );

}


function cameraStopped() {

    console.log(
        "Face Recognition Camera Stopped"
    );

}