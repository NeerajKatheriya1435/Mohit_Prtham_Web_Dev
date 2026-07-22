let mybooks=JSON.parse(localStorage.getItem("books")) || []

displayBooks()
console.log(localStorage.getItem("books"))
let editIndex = -1;

function saveNote(){
    let bookName=document.getElementById("bookName").value.trim()
    let bookAuthor=document.getElementById("bookAuthor").value.trim()
    
    if(bookName==="" || bookAuthor===""){
        alert("Please fill the entry")
        return;
    }

    if(editIndex===-1){
        mybooks.push({
            book:bookName,
            author:bookAuthor
        })
    }
    else{
        mybooks[editIndex].book=bookName
        mybooks[editIndex].author=bookAuthor
        editIndex=-1
        document.getElementById("saveBtn").innerHTML="Add Book"
    }

    localStorage.setItem("books", JSON.stringify(mybooks));
    clearForm()
    displayBooks()
}

function displayBooks(){
    let table=""
    mybooks.forEach((item,index)=>{
        table+=`
        <tr>
            <td>${index + 1}</td>
            <td>${item.book}</td>
            <td>${item.author}</td>

            <td>
                <button class="edit"
                onclick="editBook(${index})">
                Edit
                </button>

                <button class="delete"
                onclick="deleteBook(${index})">
                Delete
                </button>
            </td>
        </tr>
        `
    });

    document.getElementById("bookManager").innerHTML = table;
}

// UPDATE
function editBook(index) {

    document.getElementById("bookName").value = mybooks[index].book;

    document.getElementById("bookAuthor").value = mybooks[index].author;

    editIndex = index;

    document.getElementById("saveBtn").innerText = "Update Book";

}



// DELETE
function deleteBook(index) {

    mybooks.splice(index,1)
    localStorage.setItem("books", JSON.stringify(mybooks));
    displayBooks()

}

// SEARCH
function searchBook() {

    let search = document.getElementById("search").value.toLowerCase();

    console.log(search)
    let rows = document.querySelectorAll("#bookManager tr");

    console.log(rows)
    rows.forEach(row => {

        let book = row.cells[1].innerText.toLowerCase();
        let author = row.cells[2].innerText.toLowerCase();

        if (book.includes(search) || author.includes(search)) {
            row.style.display = "";
        }
        else {
            row.style.display = "none";
        }

    });

}
// // Clear Form

function clearForm() {

    document.getElementById("bookName").value = "";
    document.getElementById("bookAuthor").value = "";

}

