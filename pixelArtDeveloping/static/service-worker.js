if(!self.define){let e,s={};const t=(t,i)=>(t=new URL(t+".js",i).href,s[t]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=t,e.onload=s,document.head.appendChild(e)}else e=t,importScripts(t),s()})).then((()=>{let e=s[t];if(!e)throw new Error(`Module ${t} didn’t register its module`);return e})));self.define=(i,n)=>{const r=e||("document"in self?document.currentScript.src:"")||location.href;if(s[r])return;let c={};const o=e=>t(e,r),l={module:{uri:r},exports:c,require:o};s[r]=Promise.all(i.map((e=>l[e]||o(e)))).then((e=>(n(...e),c)))}}define(["./workbox-5b385ed2"],(function(e){"use strict";e.setCacheNameDetails({prefix:"frontend"}),self.addEventListener("message",(e=>{e.data&&"SKIP_WAITING"===e.data.type&&self.skipWaiting()})),e.precacheAndRoute([{url:"static/app.a920f65397551c6a.css",revision:null},{url:"static/css/app.a920f653.css",revision:null},{url:"static/index.html",revision:"4425cd980f04e8e01ee63732f0051f78"},{url:"static/js/app.76cedf88.js",revision:null},{url:"static/js/chunk-vendors.9431d1ea.js",revision:null},{url:"static/manifest.json",revision:"4b14c64efaf846819b9a229b4193c8b7"},{url:"static/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"}],{})}));
//# sourceMappingURL=service-worker.js.map
