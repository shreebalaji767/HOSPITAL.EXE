const NONREPEAT_KEY='hospital-exe-history-v3';
let history={};
function loadHistory(){try{const raw=JSON.parse(localStorage.getItem(NONREPEAT_KEY)||'{}');history=raw&&typeof raw==='object'?raw:{}}catch{history={}}}
function itemKey(value){return typeof value==='string'?value:JSON.stringify(value)}
function nextUnique(pool,key){
  if(!Array.isArray(pool)||!pool.length)return null;
  let used=Array.isArray(history[key])?history[key]:[];
  const keys=pool.map(itemKey);
  used=used.filter(id=>keys.includes(id));
  let available=pool.filter(item=>!used.includes(itemKey(item)));
  if(!available.length){used=[];available=pool.slice()}
  const picked=available[Math.floor(Math.random()*available.length)];
  used.push(itemKey(picked));history[key]=used;
  try{localStorage.setItem(NONREPEAT_KEY,JSON.stringify(history))}catch{}
  return picked;
}
function sampleUnique(pool,count,key){
  if(!Array.isArray(pool)||!pool.length)return [];
  let used=Array.isArray(history[key])?history[key]:[];
  const keys=pool.map(itemKey); used=used.filter(id=>keys.includes(id));
  let available=pool.filter(item=>!used.includes(itemKey(item)));
  if(available.length<count){used=[];available=pool.slice()}
  for(let i=available.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[available[i],available[j]]=[available[j],available[i]]}
  const picked=available.slice(0,count);used.push(...picked.map(itemKey));history[key]=used;
  try{localStorage.setItem(NONREPEAT_KEY,JSON.stringify(history))}catch{}
  return picked;
}
function clearContentHistory(){history={};try{localStorage.removeItem(NONREPEAT_KEY)}catch{}}
loadHistory();
const menu=document.querySelector('.menu-toggle');const nav=document.querySelector('.site-header nav');if(menu&&nav){menu.addEventListener('click',()=>nav.classList.toggle('open'))}

const chaos=document.getElementById('chaos-button'),title=document.getElementById('status-title'),message=document.getElementById('status-message');
const events=window.HOSPITAL_CONTENT.chaos;
let chaosCount=0;if(chaos){chaos.addEventListener('click',()=>{chaosCount++;const e=nextUnique(events,'chaos');title.textContent=e[0];message.textContent=e[1];chaos.textContent=chaosCount>5?'You have done enough.':'Increase Chaos';saveState()})}

const worldLevel=document.getElementById('world-level'),worldProgress=document.getElementById('world-progress'),worldLog=document.getElementById('world-log');
const worldNames=window.HOSPITAL_CONTENT.worldNames;
const worldActions=window.HOSPITAL_CONTENT.activities;
let worldState={level:1,progress:0,built:[]};
try{worldState={...worldState,...JSON.parse(localStorage.getItem('hospital-exe-world')||'{}')}}catch{}
function saveWorld(){try{localStorage.setItem('hospital-exe-world',JSON.stringify(worldState))}catch{}}
function renderWorld(){if(!worldLevel)return;worldLevel.textContent='HOSPITAL LEVEL '+String(worldState.level).padStart(2,'0');worldProgress.style.width=Math.min(100,Math.max(8,worldState.progress))+'%';worldLog.textContent=worldState.built.length?'BUILD LOG: '+worldState.built[worldState.built.length-1]: 'BOOT: fictional construction system online.'}
function command(action){if(!worldLevel)return;const name=nextUnique(worldNames,'worldNames');if(action==='build'){worldState.built.push(name);worldState.progress+=18;if(worldState.progress>=100){worldState.level++;worldState.progress=0;worldState.built=[];worldLog.textContent='LEVEL UP: the hospital has built something it cannot explain.'}else worldLog.textContent='BUILD: '+name+' '+worldActions[0]+'.'}if(action==='upgrade'){worldState.progress=Math.min(99,worldState.progress+12);worldLog.textContent='UPGRADE: installed technology nobody requested.'}if(action==='spawn'){worldState.progress=Math.min(99,worldState.progress+7);worldLog.textContent='SPAWN: a fictional specialist has entered the wrong department.'}if(action==='incident'){worldState.progress=Math.min(99,worldState.progress+5);worldLog.textContent='INCIDENT: '+nextUnique(worldActions,'worldActions')+'.'}saveWorld();renderWorld()}
document.querySelectorAll('[data-command]').forEach(b=>b.addEventListener('click',()=>command(b.dataset.command)));renderWorld();
document.querySelectorAll('.chaos-trigger').forEach(btn=>btn.addEventListener('click',()=>{alert(nextUnique(window.HOSPITAL_CONTENT.doctorReplies,'doctorReplies'));}));

const statusEl=document.getElementById('live-status-grid'),statusTitle=document.getElementById('live-status-title'),stamp=document.getElementById('status-timestamp');
const departments=window.HOSPITAL_CONTENT.departments;
const states=window.HOSPITAL_CONTENT.states;
const activities=window.HOSPITAL_CONTENT.activities;
function generateStatus(){if(!statusEl)return;const selected=sampleUnique(departments,8,'liveDepartments'),used=new Set();statusEl.innerHTML=selected.map((dept,i)=>{let state=nextUnique(states,'liveStates');while(used.has(state)){state=nextUnique(states,'liveStates')}used.add(state);const activity=nextUnique(activities,'liveActivities');return '<article class="live-card"><span class="live-number">'+String(i+1).padStart(2,'0')+'</span><div><strong>'+dept+'</strong><b>'+state+'</b><p>'+activity+'.</p></div></article>'}).join('');statusTitle.textContent=nextUnique(window.HOSPITAL_CONTENT.statusTitles,'statusTitles');stamp.textContent='Last fictional update: '+new Date().toLocaleTimeString([], {hour:'2-digit',minute:'2-digit',second:'2-digit'})+' • Auto-refresh: 12 seconds';saveState()}
setInterval(generateStatus,12000);generateStatus();

const STORAGE_KEY='hospital-exe-state-v2';
function saveState(){try{localStorage.setItem(STORAGE_KEY,JSON.stringify({chaosCount,lastStatus:stamp?.textContent||'',savedAt:Date.now()}))}catch{}}
try{const saved=JSON.parse(localStorage.getItem(STORAGE_KEY)||'null');if(saved?.chaosCount){chaosCount=saved.chaosCount;if(chaos)chaos.textContent=chaosCount>5?'You have done enough.':'Increase Chaos'}}catch{}

let deferredPrompt=null;const installBtn=document.getElementById('install-app');window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();deferredPrompt=e;if(installBtn)installBtn.hidden=false});installBtn?.addEventListener('click',async()=>{if(!deferredPrompt)return;deferredPrompt.prompt();await deferredPrompt.userChoice;deferredPrompt=null;installBtn.hidden=true});window.addEventListener('appinstalled',()=>{if(installBtn)installBtn.hidden=true});

document.addEventListener('keydown',e=>{if(e.key.toLowerCase()==='p')alert('🖨️ '+nextUnique(window.HOSPITAL_CONTENT.keyboardAlerts,'keyboardP'));if(e.key.toLowerCase()==='c')alert('💥 '+nextUnique(window.HOSPITAL_CONTENT.keyboardAlerts,'keyboardC'))});
setInterval(()=>{if(!document.hidden&&Math.random()<.18){alert(nextUnique(window.HOSPITAL_CONTENT.notifications,'notifications'))}},15000);

if('serviceWorker' in navigator){window.addEventListener('load',()=>navigator.serviceWorker.register('./sw.js').catch(()=>{}));}

/* PLAYABLE HOSPITAL BUILDER */
const GAME_KEY='hospital-exe-builder-v1';
const defaultGame={money:500,staff:3,power:100,chaos:0,level:1,score:0,selected:'reception',tiles:Array(20).fill(null),log:'BOOT: construction permits have been misplaced.'};
let gameState={...defaultGame};try{gameState={...defaultGame,...JSON.parse(localStorage.getItem(GAME_KEY)||'{}')}}catch{}
const gameTiles=document.getElementById('build-grid'),options=document.getElementById('build-options');
const gm=document.getElementById('game-money'),gs=document.getElementById('game-staff'),gp=document.getElementById('game-power'),gc=document.getElementById('game-chaos'),gl=document.getElementById('game-level'),glog=document.getElementById('game-log'),ut=document.getElementById('unlock-title'),ux=document.getElementById('unlock-text'),up=document.getElementById('unlock-progress');
const buildings=[{id:'reception',name:'Reception',icon:'🧑‍💼',cost:50,power:2,staff:0,unlock:1},{id:'lab',name:'Chaos Lab',icon:'🧪',cost:90,power:8,staff:1,unlock:1},{id:'tea',name:'Tea Dept.',icon:'☕',cost:70,power:1,staff:0,unlock:1},{id:'printer',name:'Printer ICU',icon:'🖨️',cost:110,power:12,staff:1,unlock:1},{id:'radiology',name:'Radiology',icon:'🩻',cost:140,power:16,staff:1,unlock:1},{id:'emergency',name:'Emergency Tower',icon:'🚑',cost:180,power:22,staff:2,unlock:2},{id:'pharmacy',name:'Quantum Pharmacy',icon:'💊',cost:220,power:26,staff:2,unlock:3},{id:'icu',name:'Infinite ICU',icon:'🏥',cost:280,power:32,staff:3,unlock:4},{id:'portal',name:'Portal Ward',icon:'🌀',cost:350,power:40,staff:4,unlock:5}];
function saveGame(){try{localStorage.setItem(GAME_KEY,JSON.stringify(gameState))}catch{}}
function unlocked(b){return gameState.level>=b.unlock}
function renderGame(){if(!gameTiles)return;gm.textContent=gameState.money;gs.textContent=gameState.staff;gp.textContent=Math.max(0,gameState.power)+'%';gc.textContent=gameState.chaos;gl.textContent=String(gameState.level).padStart(2,'0');glog.textContent=gameState.log;gameTiles.innerHTML=gameState.tiles.map((id,i)=>{const b=buildings.find(x=>x.id===id);return '<button class="build-tile '+(b?'occupied':'')+'" data-slot="'+i+'">'+(b?'<span class="tile-icon">'+b.icon+'</span><small>'+b.name+'</small>':'<span class="tile-icon">＋</span><small>EMPTY</small>')+'</button>'}).join('');gameTiles.querySelectorAll('.build-tile').forEach(t=>t.addEventListener('click',()=>buildAt(+t.dataset.slot)));const available=buildings.filter(b=>unlocked(b)&&!gameState.tiles.includes(b.id));options.innerHTML=available.map(b=>'<button class="build-option '+(gameState.selected===b.id?'selected':'')+'" data-build="'+b.id+'"><b>'+b.icon+' '+b.name+'</b><small>💰 '+b.cost+' • ⚡ '+b.power+' • 👥 '+b.staff+'</small></button>').join('');options.querySelectorAll('.build-option').forEach(b=>b.addEventListener('click',()=>{gameState.selected=b.dataset.build;renderGame()}));const next=buildings.find(b=>b.unlock>gameState.level);if(next){ut.textContent='Next unlock: '+next.name;ux.textContent='Reach Level '+next.unlock+' to unlock '+next.name+'.';up.style.width=Math.min(100,((gameState.level-1)/(next.unlock-1))*100)+'%'}else{ut.textContent='ALL SYSTEMS UNLOCKED';ux.textContent='The hospital has become legally unexplainable.';up.style.width='100%'}saveGame()}
function buildAt(slot){if(gameState.tiles[slot]){gameState.log='DEMOLITION DENIED: the building has developed emotional attachment.';renderGame();return}const b=buildings.find(x=>x.id===gameState.selected);if(!b)return;if(gameState.tiles.includes(b.id)){gameState.log='DUPLICATE DENIED: '+b.name+' already exists in this hospital.';renderGame();return;}if(gameState.money<b.cost){gameState.log='BUDGET ERROR: the hospital cannot afford '+b.name+'.';renderGame();return}gameState.money-=b.cost;gameState.staff+=b.staff;gameState.power=Math.max(0,gameState.power-b.power);gameState.score+=b.cost;gameState.tiles[slot]=b.id;if(gameState.score>=350*gameState.level){gameState.level++;gameState.money+=120;gameState.log='LEVEL UP: '+b.name+' triggered an unnecessary expansion. BONUS +120.'}else gameState.log='BUILD COMPLETE: '+b.name+' installed. Nobody read the manual.';renderGame()}
document.getElementById('incident-button')?.addEventListener('click',()=>{const incidents=window.HOSPITAL_CONTENT.chaos.map((x,i)=>[x[0],x[1],-10-(i%5)*7,5+(i%8)]);const e=nextUnique(incidents,'gameIncidents');gameState.money=Math.max(0,gameState.money+e[2]);gameState.chaos+=e[3];gameState.log='DISASTER: '+e[0]+' — '+e[1]+' '+e[2]+' budget.';if(gameState.chaos>=50){gameState.level++;gameState.chaos=0;gameState.money+=150;gameState.log+=' CHAOS LEVEL-UP! Emergency funding: +150.'}renderGame()});
document.getElementById('reset-game')?.addEventListener('click',()=>{if(confirm('Erase the fictional hospital and start over?')){gameState={...defaultGame,tiles:Array(20).fill(null)};renderGame()}});
renderGame();

window.addEventListener('storage',e=>{
  if(e.key===NONREPEAT_KEY){loadHistory()}
  if(e.key===GAME_KEY){try{gameState={...defaultGame,...JSON.parse(e.newValue||'{}')};renderGame()}catch{}}
  if(e.key==='hospital-exe-world'){try{worldState={...worldState,...JSON.parse(e.newValue||'{}')};renderWorld()}catch{}}
});
