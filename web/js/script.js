"use strict";

document.querySelector(".form").addEventListener("submit", async (e) => {
    e.preventDefault();
    let picked_product = document.querySelector('input[name="product"]:checked');
    let ticket = document.querySelector('#ticket');
    if (picked_product && ticket) {
        let res = await eel.info_product(picked_product.value, ticket.value.toUpperCase())();
        document.querySelector("#status").textContent = res["status"]
        try {
            document.querySelector(".info").remove();
        } catch (err) {
            console.log("Первое вхождение");
        }
        let info = document.createElement("div");
        info.classList.add("info");
        info.innerHTML = "";
        document.querySelector("body").appendChild(info);
        if (picked_product.value == "stocks") {
            let header = document.createElement("h2");
            header.textContent = "Анализ по техническим индикаторам(на основе осцилляторов и на основе скользящих средних)";
            document.querySelector(".info").appendChild(header);
            let wrapper = document.createElement("div");
            wrapper.classList.add("info_wrapper");
            document.querySelector(".info").appendChild(wrapper);
            for (let i of ["oscillators", "moving_averages"]) {
                let info_block = document.createElement("div");
                info_block.classList.add("info_block");
                let html = `<h3>Рекомендованно(${i}): ${res[i]['RECOMMENDATION']}</h3>`;
                html += "<ul>";
                for (let key in res[i]["COMPUTE"]) {
                    html += `<li>${key} - ${res[i]["COMPUTE"][key]}</li>`;
                }
                html += "</ul>";
                html += `<p>BUY - ${res[i]['BUY']}, SELL - ${res[i]['SELL']}, NEUTRAL - ${res[i]['NEUTRAL']}</p>`;
                info_block.innerHTML = html;
                document.querySelector(".info_wrapper").appendChild(info_block);
            }
        }
    } else {
        document.querySelector("#status").textContent = "Не выбран продукт или неверно введён тикет!"
    }
})