from pathlib import Path

path = Path('teste-v2.html')
s = path.read_text(encoding='utf-8')

marker = '/* PREVIEW-V22-COMERCIAL */'
if marker not in s:
    css = '''
/* PREVIEW-V22-COMERCIAL */
.portfolio-toolbar{display:flex;gap:10px;flex-wrap:wrap;margin:-10px 0 26px}
.portfolio-chip{padding:9px 13px;border-radius:999px;border:1px solid var(--line);background:rgba(255,255,255,.025);color:#cbd4df;font-size:10px;font-weight:900;letter-spacing:.04em}
.portfolio-chip.active{background:linear-gradient(135deg,var(--gold2),#b58b3f);color:#07111f;border-color:transparent}
.quick-quote{display:grid;grid-template-columns:.82fr 1.18fr;gap:32px;align-items:start}
.quote-intro{position:sticky;top:120px;padding:30px;border:1px solid var(--line);border-radius:26px;background:linear-gradient(145deg,#0b2542,#041326);box-shadow:0 24px 60px rgba(0,0,0,.24)}
.quote-intro p{color:var(--muted)}
.quote-badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:20px}
.quote-badges span{padding:7px 10px;border-radius:999px;border:1px solid var(--line);font-size:10px;color:#ccd5df}
.quote-form{padding:30px;border:1px solid var(--line);border-radius:26px;background:linear-gradient(145deg,#081b31,#041326);box-shadow:0 24px 60px rgba(0,0,0,.22)}
.form-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.field{display:grid;gap:7px}.field.full{grid-column:1/-1}
.field label{font-size:10px;font-weight:950;letter-spacing:.08em;text-transform:uppercase;color:var(--gold2)}
.field input,.field select,.field textarea{width:100%;border:1px solid rgba(216,184,108,.20);border-radius:13px;background:#03101f;color:#f8fafc;padding:13px 14px;font:inherit;font-size:13px;outline:none}
.field input:focus,.field select:focus,.field textarea:focus{border-color:rgba(245,221,161,.55);box-shadow:0 0 0 3px rgba(216,184,108,.08)}
.field textarea{min-height:110px;resize:vertical}
.quote-form .btn{margin-top:18px;width:100%;min-height:54px}
.form-note{font-size:10px;color:#9fabb9;margin-top:11px;text-align:center}
@media(max-width:980px){.quick-quote{grid-template-columns:1fr}.quote-intro{position:relative;top:auto}.form-grid{grid-template-columns:1fr}}
'''
    s = s.replace('</style>', css + '\n</style>', 1)

if 'PORTFOLIO-V22-TOOLBAR' not in s:
    toolbar = '''<!-- PORTFOLIO-V22-TOOLBAR -->
    <div class="portfolio-toolbar">
      <span class="portfolio-chip active">Todos</span>
      <span class="portfolio-chip">Fachadas</span>
      <span class="portfolio-chip">Arquitetônico</span>
      <span class="portfolio-chip">Estrutural</span>
      <span class="portfolio-chip">Instalações</span>
    </div>
    <div class="portfolio">'''
    s = s.replace('<div class="portfolio">', toolbar, 1)

if 'id="orcamento-rapido"' not in s:
    quote = '''<section class="section alt" id="orcamento-rapido">
  <div class="container quick-quote">
    <div class="quote-intro">
      <div class="kicker">Orçamento rápido</div>
      <h2>Conte um pouco sobre o seu projeto.</h2>
      <p>Preencha as informações principais e o site prepara uma mensagem organizada para enviar pelo WhatsApp da MN Engenharia.</p>
      <div class="quote-badges"><span>Projetos</span><span>Construção</span><span>Gerenciamento</span><span>Vistorias</span></div>
    </div>
    <form class="quote-form" id="quoteForm">
      <div class="form-grid">
        <div class="field"><label for="qNome">Nome</label><input id="qNome" required placeholder="Seu nome"></div>
        <div class="field"><label for="qCidade">Cidade</label><input id="qCidade" required placeholder="Ex.: Itumbiara - GO"></div>
        <div class="field"><label for="qServico">Serviço</label><select id="qServico" required><option value="">Selecione</option><option>Projeto de engenharia</option><option>Construção</option><option>Gerenciamento / acompanhamento</option><option>Vistoria técnica</option><option>Projeto + obra</option><option>Outro</option></select></div>
        <div class="field"><label for="qMetragem">Metragem aproximada</label><input id="qMetragem" placeholder="Ex.: 180 m²"></div>
        <div class="field"><label for="qFase">Fase atual</label><select id="qFase"><option>Estou começando / tenho uma ideia</option><option>Já tenho terreno</option><option>Já tenho projeto</option><option>Obra em andamento</option><option>Preciso avaliar um problema</option></select></div>
        <div class="field"><label for="qPrazo">Quando pretende começar?</label><select id="qPrazo"><option>O quanto antes</option><option>Nos próximos 30 dias</option><option>Em 2 a 3 meses</option><option>Mais adiante</option><option>Ainda estou planejando</option></select></div>
        <div class="field full"><label for="qDetalhes">Detalhes</label><textarea id="qDetalhes" placeholder="Conte resumidamente o que você precisa."></textarea></div>
      </div>
      <button class="btn btn-primary" type="submit">Enviar pedido pelo WhatsApp →</button>
      <div class="form-note">O WhatsApp abre com a mensagem pronta para você revisar antes do envio.</div>
    </form>
  </div>
</section>
'''
    s = s.replace('<section class="section alt" id="instagram">', quote + '\n<section class="section alt" id="instagram">', 1)

if 'href="#orcamento-rapido"' not in s:
    s = s.replace('<a href="#processo">Como trabalhamos</a>', '<a href="#processo">Como trabalhamos</a>\n      <a href="#orcamento-rapido">Orçamento rápido</a>', 1)

if 'ORCAMENTO-V22-SCRIPT' not in s:
    script = '''<script>
// ORCAMENTO-V22-SCRIPT
const quoteForm=document.getElementById('quoteForm');
if(quoteForm){quoteForm.addEventListener('submit',function(e){
  e.preventDefault();
  const v=id=>document.getElementById(id)?.value?.trim()||'Não informado';
  const msg=['Olá, vim pelo site da MN Engenharia e gostaria de solicitar um orçamento.','','Nome: '+v('qNome'),'Cidade: '+v('qCidade'),'Serviço: '+v('qServico'),'Metragem aproximada: '+v('qMetragem'),'Fase atual: '+v('qFase'),'Previsão para começar: '+v('qPrazo'),'Detalhes: '+v('qDetalhes')].join('\\n');
  window.open('https://wa.me/5564993191135?text='+encodeURIComponent(msg),'_blank','noopener');
});}
</script>
'''
    s = s.replace('</body>', script + '\n</body>', 1)

path.write_text(s, encoding='utf-8')
