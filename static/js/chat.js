console.log("App is running...")

// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: "POST", // *GET, POST, PUT, DELETE, etc.
        headers: {
            "Content-Type": "application/json",
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}

// Http get request using parameters
const get_query = async (url, params) => {
    const response = await fetch(url + '?' + new URLSearchParams(params))
    const data = await response.json()

    return data
}

// Http get request using parameters
const get_data = async (url) => {
    const response = await fetch(url)
    const data = await response.json()

    return data
}



const chatContainer = document.getElementById("inner-chat-container")

const parentChatContainer = document.getElementById("chat-container")

const loading = `
                <div class="text-center">
                <img src="../static/Infinity-2s-48px.gif" class="mx-auto d-block"  alt="">
                </div>
                `
const loading2 = `
        <div class="mx-auto text-center"> 
<div class="loadingio-spinner-dual-ball-yx9hriacfm"><div class="ldio-ibbgzpzkl2a">
<div></div><div></div><div></div>
</div></div></div>
                `
const spinner = `
        <div class="d-flex justify-content-center">
        <div class="spinner-grow text-success text-center mx-auto" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
</div>

        `


userEntry = (text) => {



    // User entry
    let userDiv = document.createElement("div")
    userDiv.id = "user-ui"
    userDiv.innerHTML = `
                <div class="card border border-0 my-3 bg-primary bg-opacity-10">
                <div class="card-body">
                    ${text}
                </div>
                </div>
            `
    chatContainer.appendChild(userDiv)


    let loadDiv = document.createElement("div")
    loadDiv.id = "load-ui"
    loadDiv.classList = "load-ui my-2"

    loadDiv.innerHTML = loading2;

    chatContainer.appendChild(loadDiv)

    parentChatContainer.scrollTop =
        parentChatContainer.scrollHeight - parentChatContainer.clientHeight;

}

botEntry = (response) => {

    let loadDivElement = document.querySelectorAll(".load-ui")

    let botDiv = document.createElement("div")
    botDiv.id = "bot-ui"
    botDiv.classList = "my-2"

    loadDivElement.forEach((element) => {
        element.classList = "d-none";
    })
    loadDivElement.classList = "d-none";

    

    botDiv.innerHTML = `
                <div class="card bg-light border border-0">
                    <div class="card-body" id="bot-text">
                        ${marked.parse(response)}
                    </div>
                </div>
                    `;


    chatContainer.appendChild(botDiv)

    parentChatContainer.scrollTop =
        parentChatContainer.scrollHeight - parentChatContainer.clientHeight;


}


let newMessage = document.getElementById("newMessage")
let sendMessage = document.getElementById("sendMessage")
// let userUI = document.getElementById("user-ui")
// let botUI = document.getElementById("bot-ui")



sendMessage.addEventListener("click", async (e) => {

    e.preventDefault()

    text = newMessage.value;
    console.log(text)

    if (text == "") {
        alert("Please enter your question.")
    }
    else {

        userEntry(text)

        newMessage.value = ""

        dummy_response = "Hii, best of luck for you career journey";

        bot_response = await get_query("/response", { chat: text })

        console.log(bot_response)


        bot_response = bot_response["res"]

        botEntry(bot_response)
        // botEntry(dummy_response)
    }




})


