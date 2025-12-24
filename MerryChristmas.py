<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>The Snowman I Call Mine ❄️</title>
  <style>
    :root{
      --bg1:#0b0f1a; --bg2:#120a24; --card:#0f172aee;
      --text:#e8eefc; --muted:#b7c3e6; --gold:#f5c451; --pink:#ff4d8d;
      --line: rgba(255,255,255,.12);
    }
    *{box-sizing:border-box}
    body{
      margin:0;
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
      color:var(--text);
      min-height:100vh;
      background:
        radial-gradient(1200px 800px at 20% 10%, #2a1a5c55, transparent 60%),
        radial-gradient(1000px 700px at 80% 0%, #ff4d8d22, transparent 55%),
        radial-gradient(900px 600px at 50% 90%, #f5c45122, transparent 55%),
        linear-gradient(160deg, var(--bg1), var(--bg2));
      overflow-x:hidden;
    }
    .wrap{
      max-width: 980px;
      margin: 0 auto;
      padding: 28px 18px 60px;
    }
    .topbar{
      display:flex; align-items:center; justify-content:space-between;
      gap:12px; margin-bottom: 18px;
    }
    .chip{
      display:inline-flex; align-items:center; gap:10px;
      padding:10px 14px; border:1px solid var(--line);
      border-radius:999px; background:rgba(255,255,255,.04);
      backdrop-filter: blur(10px);
      box-shadow: 0 10px 30px rgba(0,0,0,.25);
      font-size: 13px; color: var(--muted);
    }
    .btn{
      cursor:pointer;
      border:1px solid var(--line);
      background: linear-gradient(180deg, rgba(255,255,255,.08), rgba(255,255,255,.03));
      color:var(--text);
      padding:10px 12px;
      border-radius: 12px;
      font-weight: 600;
      display:inline-flex; align-items:center; gap:10px;
      transition: transform .12s ease, background .2s ease;
      user-select:none;
    }
    .btn:hover{ transform: translateY(-1px); background: rgba(255,255,255,.08); }
    .btn:active{ transform: translateY(0px) scale(.99); }

    .grid{
      display:grid;
      grid-template-columns: 1.25fr .95fr;
      gap: 16px;
    }
    @media (max-width: 880px){
      .grid{ grid-template-columns: 1fr; }
    }

    .card{
      border:1px solid var(--line);
      background: radial-gradient(900px 300px at 10% 0%, rgba(245,196,81,.10), transparent 55%),
                  radial-gradient(800px 300px at 90% 0%, rgba(255,77,141,.12), transparent 55%),
                  rgba(15,23,42,.72);
      border-radius: 22px;
      padding: 18px;
      box-shadow: 0 18px 60px rgba(0,0,0,.40);
      backdrop-filter: blur(10px);
      position:relative;
      overflow:hidden;
    }
    .shine::before{
      content:"";
      position:absolute; inset:-40% -30%;
      background: linear-gradient(120deg, transparent 40%, rgba(255,255,255,.14), transparent 60%);
      transform: rotate(10deg);
      animation: sheen 5.2s ease-in-out infinite;
      pointer-events:none;
    }
    @keyframes sheen{
      0%{ transform: translateX(-35%) rotate(10deg); opacity:.0; }
      25%{ opacity:.35; }
      50%{ transform: translateX(35%) rotate(10deg); opacity:.0; }
      100%{ transform: translateX(35%) rotate(10deg); opacity:.0; }
    }

    .poster{
      padding: 22px 20px;
      border-radius: 18px;
      border:1px solid rgba(255,255,255,.10);
      background: linear-gradient(180deg, rgba(0,0,0,.25), rgba(0,0,0,.05));
      position:relative;
    }
    .kicker{
      font-size: 12px;
      letter-spacing: .18em;
      color: var(--muted);
      text-transform: uppercase;
      display:flex; align-items:center; gap:10px;
    }
    .kicker .dot{
      width:8px; height:8px; border-radius:999px;
      background: var(--gold);
      box-shadow: 0 0 20px rgba(245,196,81,.6);
    }
    h1{
      margin: 12px 0 6px;
      font-size: 42px;
      line-height: 1.05;
      letter-spacing: -0.02em;
    }
    .sub{
      margin: 0 0 12px;
      color: var(--muted);
      font-size: 15px;
      line-height: 1.5;
    }
    .tag{
      display:flex; flex-wrap:wrap; gap:10px; margin-top: 12px;
    }
    .pill{
      padding:8px 10px;
      border-radius:999px;
      border:1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.04);
      font-size: 13px;
      color: var(--muted);
    }
    .gold{ color: var(--gold); }
    .pink{ color: var(--pink); }

    .sectionTitle{
      display:flex; align-items:center; justify-content:space-between;
      margin: 2px 0 10px;
      gap:10px;
    }
    .sectionTitle h2{
      margin:0;
      font-size: 16px;
      letter-spacing: .08em;
      text-transform: uppercase;
      color: var(--muted);
    }
    .divider{ height:1px; background: var(--line); margin: 10px 0 14px; }

    .typebox{
      font-size: 16px;
      line-height: 1.7;
      margin: 0;
      min-height: 150px;
      color: var(--text);
      white-space: pre-wrap;
    }
    .cursor{
      display:inline-block;
      width: 9px; height: 18px;
      background: rgba(255,255,255,.65);
      margin-left: 4px;
      transform: translateY(2px);
      animation: blink .9s steps(2) infinite;
    }
    @keyframes blink{ 50%{ opacity:0; } }

    .ticket{
      border-radius: 18px;
      border:1px dashed rgba(255,255,255,.18);
      background: rgba(0,0,0,.18);
      padding: 14px;
      position:relative;
      overflow:hidden;
    }
    .ticketRow{
      display:grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 10px;
    }
    .field{
      border:1px solid rgba(255,255,255,.10);
      border-radius: 14px;
      padding: 10px 12px;
      background: rgba(255,255,255,.03);
    }
    .label{
      font-size: 11px;
      letter-spacing: .14em;
      text-transform: uppercase;
      color: var(--muted);
      margin-bottom: 6px;
    }
    .value{
      font-size: 14px;
      color: var(--text);
      font-weight: 600;
      line-height: 1.35;
    }
    .stars{
      font-size: 14px;
      color: var(--gold);
      letter-spacing: .08em;
    }

    .photos{
      display:grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-top: 12px;
    }
    .ph{
      border-radius: 16px;
      border:1px solid rgba(255,255,255,.12);
      background: rgba(255,255,255,.05);
      height: 120px;
      display:flex; align-items:center; justify-content:center;
      color: rgba(255,255,255,.35);
      font-size: 12px;
      overflow:hidden;
      position:relative;
    }
    .ph img{
      width:100%; height:100%;
      object-fit: cover;
      display:block;
      filter: saturate(1.05) contrast(1.02);
      transform: scale(1.01);
    }

    .footerNote{
      margin-top: 14px;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.55;
    }

    /* confetti */
    canvas#fx{
      position: fixed;
      inset:0;
      pointer-events:none;
      z-index: 50;
    }

    /* tiny heart float */
    .floaty{
      position:absolute;
      right: 16px;
      top: 14px;
      font-size: 18px;
      opacity:.85;
      animation: float 2.8s ease-in-out infinite;
      filter: drop-shadow(0 10px 18px rgba(0,0,0,.35));
    }
    @keyframes float{
      0%,100%{ transform: translateY(0); }
      50%{ transform: translateY(-8px); }
    }
  </style>
</head>
<body>
  <canvas id="fx"></canvas>

  <div class="wrap">
    <div class="topbar">
      <div class="chip">🎄 <span id="dateText"></span> • <span class="gold">Limited Release</span> • Only in <span class="pink">Your Heart</span></div>
      <div style="display:flex; gap:10px; flex-wrap:wrap;">
        <div class="btn" id="playBtn">✨ Play Trailer</div>
        <div class="btn" id="confettiBtn">🎉 Make it Rain</div>
      </div>
    </div>

    <div class="grid">
      <!-- LEFT: poster + letter -->
      <div class="card shine">
        <div class="floaty">☃️💖</div>
        <div class="poster">
          <div class="kicker"><span class="dot"></span> NOW SHOWING THIS CHRISTMAS</div>
          <h1 id="titleText">THE SNOWMAN I CALL MINE</h1>
          <p class="sub" id="subtitleText">
            Starring <span class="gold" id="hisName">[His Name]</span> • Co-starring <span class="pink">A</span><br/>
            Genre: Snowfall • Rom-Com • Comfort • Forever
          </p>
          <div class="tag">
            <div class="pill">⭐ 5/5 — “Unreal boyfriend energy”</div>
            <div class="pill">🎬 Director’s Cut: Us</div>
            <div class="pill">🍿 Runtime: All year, every year</div>
          </div>
        </div>

        <div class="divider"></div>

        <div class="sectionTitle">
          <h2>Director’s Note</h2>
          <div class="btn" id="retypeBtn">🔁 Replay Letter</div>
        </div>
        <p class="typebox" id="typebox"></p>

        <div class="footerNote">
          Tip: Customize the name + optional photos/music at the top (search for <b>EDIT ME</b>).
        </div>
      </div>

      <!-- RIGHT: ticket + photos -->
      <div class="card">
        <div class="sectionTitle">
          <h2>Premiere Ticket</h2>
          <div class="stars" aria-label="5 stars">★★★★★</div>
        </div>

        <div class="ticket">
          <div class="label">Admit One</div>
          <div class="value" id="ticketTitle">Winter Premiere: The Snowman I Call Mine</div>

          <div class="ticketRow">
            <div class="field">
              <div class="label">Seat</div>
              <div class="value" id="seatText">Right next to me (non-negotiable)</div>
            </div>
            <div class="field">
              <div class="label">Valid For</div>
              <div class="value" id="timeText">Lifetime + all re-releases</div>
            </div>
            <div class="field">
              <div class="label">Dress Code</div>
              <div class="value" id="dressText">Cozy, warm, smells like you</div>
            </div>
            <div class="field">
              <div class="label">Includes</div>
              <div class="value" id="locText">Unlimited hugs + forehead kisses + comfort</div>
            </div>
          </div>

          <div class="divider"></div>

          <div class="label">Redeem For</div>
          <div class="value" id="redeemText">
            One hug + one kiss + unlimited love (no expiry)
          </div>

          <div class="divider"></div>

          <div class="label">Fine Print</div>
          <div class="value" id="finePrint">
            Once redeemed, you’re mine. No refunds. Only love. ❄️
          </div>
        </div>

        <div class="divider"></div>

        <div class="sectionTitle">
          <h2>Our Highlights</h2>
          <div class="chip">📸 drag & drop</div>
        </div>
        <div class="photos">
          <div class="ph" id="ph1">Drop photo 1</div>
          <div class="ph" id="ph2">Drop photo 2</div>
          <div class="ph" id="ph3">Drop photo 3</div>
        </div>

        <div class="footerNote">
          Music tip: put an mp3 in the same folder as this file and set <b>MUSIC_FILE</b>. I set it to
          <b>Underneath the Tree</b> by default (if you add the mp3).
        </div>
      </div>
    </div>
  </div>

  <script>
    /***********************
     * EDIT ME (customize)
     ***********************/
    const HIS_NAME = "YOUR BOYFRIEND"; // <-- put his name here

    // Movie title (locked in ✅)
    const CARD_TITLE = "THE SNOWMAN I CALL MINE";

    // Your letter (your voice, polished but same emotion ✅)
    const LETTER = [
      `Baby boo… Hey!!! Hiii!!!`,
      `Merry Christmas!! 🎄✨`,
      ``,
      `A festivity of joy, happiness, light, laughter—and nothing but all the love in the world.`,
      `You have no idea how terribly I miss you right now, my precious baby.`,
      ``,
      `I wish we were together—hand in hand, decorating a space with cute little things, giving it a personality of us.`,
      `Sitting near the window, watching the snow shower, lost in each other’s eyes… in each other’s arms.`,
      `Ahmm baby… I love youuu 🤍`,
      ``,
      `You are, undoubtedly, the best gift I received this year—2025.`,
      `A gift I didn’t ask for, but was truly blessed with.`,
      `And now that I have all the access… I ain’t letting it slip out of my hands.`,
      `You’re that soul I’d want to preserve with all of me.`,
      ``,
      `I’m grateful—for that reply you shot on my story.`,
      `For us talking.`,
      `For the first time listening to you.`,
      `For the feeling of wanting more.`,
      ``,
      `For the craziness.`,
      `For the music audition and those music conversations.`,
      `For our first meet—the buzz, the awkwardness, that very first awkward hug.`,
      `For the acknowledgment.`,
      `For the thought of a second meet.`,
      `For trying to fix that hug.`,
      ``,
      `For the sleepless nights.`,
      `For the nights I looked forward to.`,
      `For slowing and easing my nights.`,
      `For sacrificing your sleep.`,
      `For listening to all my rants, loose talks, gyan, and what not.`,
      ``,
      `For the Bollywood craze.`,
      `For those unbelievable coincidence campus meets—especially the day I was coming to Portland.`,
      `For singing with me.`,
      `For bringing me food.`,
      `For boozing with me.`,
      `For making the move.`,
      ``,
      `For always being with me.`,
      `For listening to me.`,
      `For holding me.`,
      `For the comfort.`,
      `For making me feel like home.`,
      `For agreeing to all my crazy-ass thoughts.`,
      `For always trying to come up with a solution.`,
      `For making me a better being.`,
      ``,
      `I don’t think I could ever get enough of you now—`,
      `never… until February 31st arrives, baby.`,
      ``,
      `You are special.`,
      `Trust me—I’m not saying this just because you’re my boyfriend.`,
      `You are genuinely the special one.`,
      `Even when things get a bit annoying or irritating, you bring so much happiness into everyone’s life.`,
      ``,
      `I’m glad I found my hetav for life.`,
      `I wish you all the love, light, and wellness—for everything you think, pursue, execute, and beyond.`,
      ``,
      `Love,`,
      `A 🤍`
    ].join("\n");

    // Music choices:
    // If you want "Underneath the Tree" (Kelly Clarkson), drop an mp3 in the same folder and name it exactly:
    //   underneath_the_tree.mp3
    // If you prefer Sia "Snowman", use:
    //   snowman.mp3
    const MUSIC_FILE = "underneath_the_tree.mp3"; // <-- you said your heart is on this 🎶

    // Optional photos (or drag & drop at runtime)
    const PHOTOS = ["", "", ""]; // e.g. ["p1.jpg","p2.jpg","p3.jpg"]

    /***********************
     * Logic
     ***********************/
    const $ = (id) => document.getElementById(id);

    // date chip
    const now = new Date();
    $("dateText").textContent = now.toLocaleDateString(undefined, { weekday:"long", month:"short", day:"numeric", year:"numeric" });

    // text inject
    $("hisName").textContent = HIS_NAME;
    $("titleText").textContent = CARD_TITLE;

    const subtitle = `Starring ${HIS_NAME} • Co-starring A`;
    $("subtitleText").innerHTML = `${subtitle}<br/>Genre: Snowfall • Rom-Com • Comfort • Forever`;

    // Ticket inject
    $("ticketTitle").textContent = "Winter Premiere: The Snowman I Call Mine";

    // photos (optional preload)
    const photoEls = [$("ph1"), $("ph2"), $("ph3")];
    PHOTOS.forEach((src, i) => {
      if(src){
        const img = document.createElement("img");
        img.src = src;
        img.alt = `Photo ${i+1}`;
        photoEls[i].innerHTML = "";
        photoEls[i].appendChild(img);
      }
    });

    // typewriter
    let typing = null;
    function typewrite(text){
      if(typing) clearInterval(typing);
      const box = $("typebox");
      box.textContent = "";
      let i = 0;
      const cursor = document.createElement("span");
      cursor.className = "cursor";
      box.appendChild(cursor);

      typing = setInterval(() => {
        cursor.remove();
        box.textContent = box.textContent + text[i];
        box.appendChild(cursor);
        i++;
        if(i >= text.length){
          clearInterval(typing);
          cursor.remove();
        }
      }, 16);
    }
    typewrite(LETTER);

    $("retypeBtn").addEventListener("click", () => typewrite(LETTER));

    // mini “trailer” effect = confetti + spotlight + optional music toggle
    let audio = null;
    if(MUSIC_FILE){
      audio = new Audio(MUSIC_FILE);
      audio.loop = true;
      audio.volume = 0.35;
    }

    $("playBtn").addEventListener("click", () => {
      burstConfetti(160);
      pulseTitle();
      if(audio){
        if(audio.paused) audio.play();
        else audio.pause();
      }
      $("playBtn").textContent = audio ? (audio.paused ? "✨ Play Trailer" : "⏸ Pause Trailer") : "✨ Play Trailer";
    });

    $("confettiBtn").addEventListener("click", () => burstConfetti(260));

    function pulseTitle(){
      const el = $("titleText");
      el.animate(
        [
          { transform:"scale(1)", filter:"drop-shadow(0 0 0 rgba(245,196,81,0))" },
          { transform:"scale(1.02)", filter:"drop-shadow(0 14px 26px rgba(245,196,81,.25))" },
          { transform:"scale(1)", filter:"drop-shadow(0 0 0 rgba(245,196,81,0))" }
        ],
        { duration: 900, easing: "cubic-bezier(.2,.8,.2,1)"}
      );
    }

    // Confetti canvas
    const canvas = $("fx");
    const ctx = canvas.getContext("2d");
    let W, H;

    function resize(){
      W = canvas.width = window.innerWidth * devicePixelRatio;
      H = canvas.height = window.innerHeight * devicePixelRatio;
    }
    window.addEventListener("resize", resize);
    resize();

    let particles = [];
    function burstConfetti(count=180){
      const originX = W * 0.5;
      const originY = H * 0.20;
      for(let i=0;i<count;i++){
        particles.push({
          x: originX + rand(-80,80) * devicePixelRatio,
          y: originY + rand(-30,30) * devicePixelRatio,
          vx: rand(-5,5) * devicePixelRatio,
          vy: rand(2,8) * devicePixelRatio,
          g: rand(0.08,0.15) * devicePixelRatio,
          s: rand(6,12) * devicePixelRatio,
          a: 1,
          r: rand(0,Math.PI*2),
          vr: rand(-0.2,0.2),
          c: [ [245,196,81],[255,77,141],[232,238,252],[183,195,230] ][Math.floor(Math.random()*4)]
        });
      }
      if(!animating) animate();
    }
    function rand(a,b){ return a + Math.random()*(b-a); }

    let animating = false;
    function animate(){
      animating = true;
      ctx.clearRect(0,0,W,H);
      particles = particles.filter(p => p.a > 0.02 && p.y < H + 40*devicePixelRatio);
      for(const p of particles){
        p.vy += p.g;
        p.x += p.vx;
        p.y += p.vy;
        p.r += p.vr;
        p.a *= 0.992;

        ctx.save();
        ctx.translate(p.x,p.y);
        ctx.rotate(p.r);
        ctx.globalAlpha = p.a;
        ctx.fillStyle = `rgb(${p.c[0]},${p.c[1]},${p.c[2]})`;
        ctx.fillRect(-p.s/2, -p.s/2, p.s, p.s*0.55);
        ctx.restore();
      }
      if(particles.length){
        requestAnimationFrame(animate);
      } else {
        animating = false;
      }
    }

    // first tiny celebration
    setTimeout(() => burstConfetti(90), 500);

    // Drag & drop photos into placeholders
    photoEls.forEach((el, idx) => {
      el.addEventListener("dragover", (e)=>{ e.preventDefault(); el.style.outline="2px solid rgba(245,196,81,.6)"; });
      el.addEventListener("dragleave", ()=>{ el.style.outline="none"; });
      el.addEventListener("drop", (e)=>{
        e.preventDefault();
        el.style.outline="none";
        const file = e.dataTransfer.files?.[0];
        if(!file) return;
        const url = URL.createObjectURL(file);
        const img = document.createElement("img");
        img.src = url;
        img.alt = `Dropped photo ${idx+1}`;
        el.innerHTML = "";
        el.appendChild(img);
      });
    });
  </script>
</body>
</html>
