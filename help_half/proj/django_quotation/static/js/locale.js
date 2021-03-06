arr_us = new Array();
arr_tw = new Array();
arr_cn = new Array();

arr_us[0] = "Home";
arr_us[1] = "Partners";
arr_us[2] = "Contact";
arr_us[3] = "Language";
arr_us[4] = "Floor Quotation should be EASY and FREE!";
arr_us[5] = "You don't have to provide any personal information. Just need few clicks, you can quota the estimated cost.";
arr_us[6] = "Try Today!";
arr_us[7] = 'What is <span class="text-orange">HELP</span><span class="text-gray">HALF</span> Quotation Service ?';
arr_us[8] = "what ans?"
arr_us[9] = 'Why is <span class="text-orange">HELP</span><span class="text-gray">HALF</span> Quotation Service ?';
arr_us[10] = 'why ans?';
arr_us[11] = 'Who made <span class="text-orange">HELP</span><span class="text-gray">HALF</span> Quotation Service ?';
arr_us[12] = 'who ans?';


arr_tw[0] = "首頁";
arr_tw[1] = "合作夥伴";
arr_tw[2] = "聯絡我們";
arr_tw[3] = "選擇語系";
arr_tw[4] = "輕鬆且免費的地板詢價，是的！完全免費！";
arr_tw[5] = "您無須提供任何個人隱私，只需要短短幾個步驟，即可免費得知地板工程相關估價";
arr_tw[6] = "現在就試試！";
arr_tw[7] = '<span class="text-orange">HELP</span><span class="text-gray">HALF</span> 詢價服務是什麼?';
arr_tw[8] = "what ans?";
arr_tw[9] = '為什麼選擇<span class="text-orange"> HELP</span><span class="text-gray">HALF</span> 詢價服務?';
arr_tw[10] = 'why ans?';
arr_tw[11] = '誰製作了 <span class="text-orange">HELP</span><span class="text-gray">HALF</span> 詢價服務?';
arr_tw[12] = 'who ans?';


arr_cn[0] = "首页";
arr_cn[1] = "合作伙伴";
arr_cn[2] = "联络我们";
arr_cn[3] = "选择语系";
arr_cn[4] = "轻松且免费的地板询价，是的！完全免费！";
arr_cn[5] = "您无须提供任何个人隐私，只需要短短几个步骤，即可免费得知地板工程相关估价";
arr_cn[6] = "现在就试试！";
arr_cn[7] = '<span class="text-orange">HELP</span><span class="text-gray">HALF</span> 询价服务是什么?';
arr_cn[8] = "what ans?";
arr_cn[9] = '为什么选择<span class="text-orange"> HELP</span><span class="text-gray">HALF</span> 询价服务?';
arr_cn[10] = 'why ans?';
arr_cn[11] = '谁制作了 <span class="text-orange">HELP</span><span class="text-gray">HALF</span> 询价服务?';
arr_cn[12] = 'who ans?';

document.addEventListener("DOMContentLoaded", function() {
	var url = location.href;
	var params = url.split("?");
	var vars = params[1].split("&");
	for (var i = 0; i < vars.length; i++) {
    	var re = /(.+)=(.+)/;
    	var matchedPattern = re.exec(vars[i]);
    	if (matchedPattern[1] == 'lang') {
    		onLoadChangeLang(matchedPattern[2]);
    	}
   	};
});

function onChangePage(selected) {
	var newPage = selected.getAttribute('page');
	var url = location.href;
	var pathArr = url.split('/');
	var base = pathArr[pathArr.length - 1];
	var domain = url.substring(0, url.length - base.length);
	var params = base.split("?");
	var newUrl = domain + newPage;
	if (params[1] && params[1].length > 0) {
		newUrl = newUrl + '?' + params[1];
	}
	window.location.replace(newUrl);
}

function onLoadChangeLang(input_lang) {
	var lang;
	if (input_lang == 'tw') {
		lang = arr_tw;
	} else if (input_lang == 'cn') {
		lang = arr_cn;
	} else if (input_lang == 'en') {
		lang = arr_us;
	} else {
		lang = arr_us;
	}
	
	changeLang(lang);
}

function onClickChangeLang(selected) {
	var lang;
	var url = location.href;
	var params = url.split("?");
	var sub = 'lang='+selected.getAttribute('lang');
	var re1 = /lang=(.+)&/;
	var re2 = /lang=(.+)/;
	
	if (params.length > 1) { // we have params
		var matchedPattern1 = re1.exec(url);

		if (matchedPattern1 && matchedPattern1[1].length > 0) { // with following params
			sub = sub + '&';
			url = url.replace(re1, sub);
		} else {
			var matchedPattern2 = re2.exec(url);
			if (matchedPattern2 && matchedPattern2[1].length > 0) {
				url = url.replace(re2, sub);
			} else {
				url = url + '&' + sub;
			}
		}
	} else {
		url = url + '?lang=' + selected.getAttribute('lang');
	}    
	window.location.replace(url);
}

function changeLang(lang) {
	document.getElementById('home').innerHTML = lang[0];
	document.getElementById('partners').innerHTML = lang[1];
	document.getElementById('contact').innerHTML = lang[2];
	document.getElementById('language').innerHTML = lang[3];
	document.getElementById('slogan').innerHTML = lang[4];
	document.getElementById('subtitle').innerHTML = lang[5];
	document.getElementById('try').innerHTML = lang[6];
	document.getElementById('what').innerHTML = lang[7];
	document.getElementById('what-ans').innerHTML = lang[8];
	document.getElementById('why').innerHTML = lang[9];
	document.getElementById('why-ans').innerHTML = lang[10];
	document.getElementById('who').innerHTML = lang[11];
	document.getElementById('who-ans').innerHTML = lang[12];
}

