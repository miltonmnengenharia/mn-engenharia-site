document.addEventListener('DOMContentLoaded',()=>{const current=location.pathname.split('/').pop()||'teste-v2.html';const home='teste-v2.html';const html=`<footer class="mn-footer-v27"><div class="mnf-wrap"><div class="mnf-grid"><div><a class="mnf-brand" href="${home}" aria-label="Voltar ao início da MN Engenharia"><img src="assets/logo.webp" alt="MN Engenharia"><span>MN Engenharia</span></a><p>Projetos, construção, acompanhamento, gerenciamento de obras e vistorias técnicas com atuação principal em Itumbiara - GO e região.</p><a class="mnf-quote" href="contato.html">Solicitar orçamento →</a></div><div><h3>Serviços</h3><div class="mnf-links"><a href="projetos.html">Projetos</a><a href="construcao.html">Construção</a><a href="acompanhamento-de-obras.html">Acompanhamento de obras</a><a href="gerenciamento-de-obras.html">Gerenciamento</a><a href="vistorias-tecnicas.html">Vistorias técnicas</a></div></div><div><h3>Empresa e contato</h3><div class="mnf-links"><a href="sobre.html">Sobre a MN Engenharia</a><a href="contato.html">Contato</a><a href="tel:+5564993191135">(64) 99319-1135</a><a href="mailto:milton@mnengenharia.com.br">milton@mnengenharia.com.br</a><a href="https://www.instagram.com/mn_engenhariacivil" target="_blank" rel="noopener">@mn_engenhariacivil</a></div></div></div><div class="mnf-bottom"><span>MN Engenharia Civil LTDA • Itumbiara - GO</span><span>Prévia do novo site • conteúdo em revisão antes da publicação oficial</span></div></div></footer>`;const existing=document.querySelector('footer');if(existing){existing.outerHTML=html}else{document.body.insertAdjacentHTML('beforeend',html)}document.querySelectorAll('a.brand,a.mnf-brand').forEach(a=>{a.href=home;a.setAttribute('aria-label','Voltar ao início da MN Engenharia');a.title='Voltar ao início'});});

// SITE-V28-AUDIT-FIXES
document.addEventListener('DOMContentLoaded',()=>{
  const navlinks=document.querySelector('.navlinks');
  if(navlinks){
    const nav=navlinks.parentElement;
    if(nav && !nav.querySelector('.menu') && !nav.querySelector('.mn-menu-v28')){
      const btn=document.createElement('button');
      btn.type='button';
      btn.className='mn-menu-v28';
      btn.setAttribute('aria-label','Abrir menu');
      btn.setAttribute('aria-expanded','false');
      btn.textContent='☰';
      nav.appendChild(btn);
      btn.addEventListener('click',()=>{
        const open=navlinks.classList.toggle('open');
        btn.setAttribute('aria-expanded',String(open));
      });
      navlinks.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
        navlinks.classList.remove('open');
        btn.setAttribute('aria-expanded','false');
      }));
    }
  }

  const chips=[...document.querySelectorAll('.portfolio-chip')];
  const cards=[...document.querySelectorAll('.project-card')];
  if(chips.length && cards.length){
    const normalize=t=>t.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
    const applyFilter=chip=>{
      const selected=normalize(chip.textContent.trim());
      chips.forEach(c=>{
        const active=c===chip;
        c.classList.toggle('active',active);
        c.setAttribute('aria-pressed',String(active));
      });
      cards.forEach(card=>{
        const hay=normalize(card.textContent);
        const architectural=selected==='arquitetonico' && (hay.includes('arquitetonico')||hay.includes('arquitetura'));
        const show=selected==='todos' || hay.includes(selected) || architectural;
        card.hidden=!show;
      });
    };
    chips.forEach(chip=>{
      chip.setAttribute('role','button');
      chip.setAttribute('tabindex','0');
      chip.setAttribute('aria-pressed',String(chip.classList.contains('active')));
      chip.addEventListener('click',()=>applyFilter(chip));
      chip.addEventListener('keydown',e=>{
        if(e.key==='Enter'||e.key===' '){e.preventDefault();applyFilter(chip);}
      });
    });
  }
});
