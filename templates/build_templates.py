# -*- coding: utf-8 -*-
"""
Perfect_Web 참고 디자인 — 업종별 데모 페이지 만들기

    python templates/build_templates.py

TEMPLATES 목록에 한 덩어리를 더 쓰면 데모가 한 장 늘어납니다.

⚠️ shop.html(농산물 몰)과 admin.html(관리자 화면)은 여기서 안 만듭니다.
   둘은 소개형 홈페이지와 구조가 완전히 달라 각자 스타일을 따로 갖습니다.
   고칠 때는 그 파일을 직접 여세요.
색·모서리는 각 항목의 'css' 한 줄만 고치면 페이지 전체가 따라 바뀝니다.
디자인 뼈대는 _style.css 하나를 다 같이 씁니다.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))


def head(t):
    return """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s | Perfect_Web 참고 디자인</title>
<meta name="description" content="%(desc)s">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://cdn.jsdelivr.net">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
%(gf)s<link rel="stylesheet" href="_style.css">
<style>:root{%(css)s}</style>
</head>
<body>
<div class="demo-bar">이 화면은 <b>Perfect_Web 참고 디자인 견본</b>입니다. 실제 업체가 아닙니다. &nbsp;<a href="../index.html#design">&larr; 목록으로</a></div>
""" % dict(t, gf=(
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=%s&display=swap" rel="stylesheet">\n'
    % t['gfont']) if t.get('gfont') else '')


def header(t):
    nav = ''.join('<a href="#%s">%s</a>' % (i, n) for i, n in t['nav'])
    return """
<header class="th">
  <div class="tw">
    <a class="lg" href="#top">%s<span>.</span></a>
    <nav>%s</nav>
    <a class="cta" href="#apply">%s</a>
  </div>
</header>
""" % (t['brand'], nav, t['cta'])


def hero(t):
    return """
<section class="thero" id="top">
  <div class="tw">
    <div>
      <p class="eb">%s</p>
      <h1>%s</h1>
      <p class="l">%s</p>
      <div class="btns">
        <a class="tb p" href="#apply">%s</a>
        <a class="tb o" href="#s1">%s</a>
      </div>
    </div>
    <div class="tart" aria-hidden="true">%s</div>
  </div>
</section>
""" % (t['eb'], t['h1'], t['lead'], t['cta'], t['cta2'], t['art'])


def cards(sid, alt, eb, h2, sub, items, cls='g3'):
    body = ''.join(
        '<div class="card"><div class="ic"></div><h3>%s</h3><p>%s</p></div>' % (a, b)
        for a, b in items)
    return """
<section class="ts%s" id="%s">
  <div class="tw">
    <div class="tsh"><p class="eb">%s</p><h2>%s</h2><p>%s</p></div>
    <div class="%s">%s</div>
  </div>
</section>
""" % (' alt' if alt else '', sid, eb, h2, sub, cls, body)


def table(sid, alt, eb, h2, sub, cols, rows):
    th = ''.join('<th>%s</th>' % c for c in cols)
    tr = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    return """
<section class="ts%s" id="%s">
  <div class="tw">
    <div class="tsh"><p class="eb">%s</p><h2>%s</h2><p>%s</p></div>
    <table class="ttab"><thead><tr>%s</tr></thead><tbody>%s</tbody></table>
  </div>
</section>
""" % (' alt' if alt else '', sid, eb, h2, sub, th, tr)


def people(sid, alt, eb, h2, sub, ppl):
    body = ''.join(
        '<div class="pp"><div class="ph"></div><div class="in"><b>%s</b><span>%s</span></div></div>' % (a, b)
        for a, b in ppl)
    return """
<section class="ts%s" id="%s">
  <div class="tw">
    <div class="tsh"><p class="eb">%s</p><h2>%s</h2><p>%s</p></div>
    <div class="ppl">%s</div>
  </div>
</section>
""" % (' alt' if alt else '', sid, eb, h2, sub, body)


def apply_sec(t):
    opts = ''.join('<option>%s</option>' % o for o in t['apply_opts'])
    return """
<section class="ts alt" id="apply">
  <div class="tw" style="max-width:720px">
    <div class="tsh"><p class="eb">%s</p><h2>%s</h2><p>%s</p></div>
    <form class="tform" onsubmit="event.preventDefault();alert('견본 화면입니다. 실제로 접수되지 않습니다.')">
      <div class="r">
        <div><label>이름</label><input placeholder="성함"></div>
        <div><label>연락처</label><input placeholder="010-0000-0000"></div>
      </div>
      <div class="r">
        <div><label>%s</label><select>%s</select></div>
        <div><label>희망 시간</label><input placeholder="예: 평일 저녁"></div>
      </div>
      <div><label>남기실 말씀</label><textarea placeholder="한두 문장이면 충분합니다."></textarea></div>
      <button class="tb p" style="justify-content:center;border:0;cursor:pointer">%s</button>
    </form>
  </div>
</section>
""" % (t['apply_eb'], t['apply_h2'], t['apply_sub'], t['apply_label'], opts, t['cta'])


def footer(t):
    return """
<footer class="tf">
  <div class="tw">
    <div><b>%s</b>%s</div>
    <div class="mark">이 페이지는 Perfect_Web 이 만든 <b style="display:inline;font-size:12.5px">참고 디자인 견본</b>입니다.<br>실제 업체·연락처가 아닙니다.</div>
  </div>
</footer>
</body>
</html>
""" % (t['brand'], t['foot'])


def phero(t):
    """사진이 꽉 찬 첫 화면. photo 가 없으면 색면으로 대신한다."""
    inner = """
    <div class="tw">
      <p class="eb">%s</p>
      <h1>%s</h1>
      <p class="l">%s</p>
      <div class="btns">
        <a class="tb p" href="#apply">%s</a>
        <a class="tb o" href="#s1">%s</a>
      </div>
    </div>
""" % (t['eb'], t['h1'], t['lead'], t['cta'], t['cta2'])
    al = (' ' + t['align']) if t.get('align') else ''
    if t.get('bare'):
        # 첫 화면에 글자를 두지 않는다. 사진만 크게 걸고 바로 아래에서 말을 시작한다.
        return ('\n<section class="phero bare" id="top" aria-hidden="true">\n'
                '  <img src="%s" alt="" loading="eager" decoding="async">\n'
                '  <div class="tw"></div>\n</section>\n'
                '<section class="bare-lead">\n  <div class="tw">\n'
                '    <div>\n      <p class="eb">%s</p>\n      <h1>%s</h1>\n    </div>\n'
                '    <div>\n      <p>%s</p>\n'
                '      <div class="btns"><a class="tb p" href="#apply">%s</a>'
                '<a class="tb o" href="#s1">%s</a></div>\n    </div>\n'
                '  </div>\n</section>\n'
                % (t['photo'], t['eb'], t['h1'], t['lead'], t['cta'], t['cta2']))
    if t.get('photo'):
        return ('\n<section class="phero%s" id="top">\n'
                '  <img src="%s" alt="" loading="eager" decoding="async">%s</section>\n'
                % (al, t['photo'], inner))
    return '\n<section class="chero%s" id="top">%s</section>\n' % (al, inner)


def statbar(items):
    """숫자 띠 — 지어낸 숫자가 아니라 그 업종이 실제로 내세울 만한 항목만 쓴다."""
    body = ''.join('<div><b>%s<i>%s</i></b><span>%s</span></div>' % (n, u, l)
                   for n, u, l in items)
    return '\n<section class="statbar"><div class="tw">%s</div></section>\n' % body


def pcards(sid, alt, eb, h2, sub, items):
    """사진이 들어간 카드. 사진이 없으면 색면으로 자리를 채운다."""
    body = ''
    for it in items:
        img = ('<img src="%s" alt="" loading="lazy" decoding="async">' % it[3]) if len(it) > 3 and it[3] else '<div class="ph"></div>'
        body += ('<div class="pcard">%s<div class="in"><span class="tagline">%s</span>'
                 '<h3>%s</h3><p>%s</p></div></div>' % (img, it[0], it[1], it[2]))
    return """
<section class="ts%s" id="%s">
  <div class="tw">
    <div class="tsh"><p class="eb">%s</p><h2>%s</h2><p>%s</p></div>
    <div class="pcards">%s</div>
  </div>
</section>
""" % (' alt' if alt else '', sid, eb, h2, sub, body)


# ── 업종별로 다르게 쓰는 칸들 ─────────────────────────────────────────
def _wrap(sid, alt, eb, h2, sub, inner):
    return ('\n<section class="ts%s" id="%s">\n  <div class="tw">\n'
            '    <div class="tsh"><p class="eb">%s</p><h2>%s</h2><p>%s</p></div>\n'
            '    %s\n  </div>\n</section>\n'
            % (' alt' if alt else '', sid, eb, h2, sub, inner))


def steps4(sid, alt, eb, h2, sub, items):
    """번호가 붙은 진행 단계. (제목, 설명, 걸리는 시간)"""
    b = ''.join('<div class="st"><span class="no">%d</span><h3>%s</h3><p>%s</p>%s</div>'
                % (i + 1, a, c, ('<span class="tm">%s</span>' % t) if t else '')
                for i, (a, c, t) in enumerate(items))
    return _wrap(sid, alt, eb, h2, sub, '<div class="steps4">%s</div>' % b)


def spec(sid, alt, eb, h2, sub, rows):
    """항목 : 값 나열. 설비 목록·견적 기준처럼 표보다 읽기 편할 때."""
    b = ''.join('<div class="row"><b>%s</b><div class="v">%s</div></div>' % (a, c)
                for a, c in rows)
    return _wrap(sid, alt, eb, h2, sub, '<div class="spec">%s</div>' % b)


def timeline(sid, alt, eb, h2, sub, rows):
    b = ''.join('<div class="it"><div class="yr">%s</div><b>%s</b><p>%s</p></div>' % r
                for r in rows)
    return _wrap(sid, alt, eb, h2, sub, '<div class="tl">%s</div>' % b)


def cases(sid, alt, eb, h2, sub, rows):
    """사례 목록 — (분류, 제목, 내용, 결과)"""
    b = ''.join('<div class="cs"><span class="kind">%s</span>'
                '<div><b>%s</b><p>%s</p></div>'
                '<div class="res"><span>결과</span>%s</div></div>' % r for r in rows)
    return _wrap(sid, alt, eb, h2, sub, '<div class="cases">%s</div>' % b)


def faq(sid, alt, eb, h2, sub, rows):
    b = ''.join('<details%s><summary>%s</summary><div class="an">%s</div></details>'
                % (' open' if i == 0 else '', q, a) for i, (q, a) in enumerate(rows))
    return _wrap(sid, alt, eb, h2, sub, '<div class="faq">%s</div>' % b)


def hours(sid, alt, eb, h2, sub, cols, rows, note=''):
    th = ''.join('<th>%s</th>' % c for c in cols)
    tr = ''
    for r in rows:
        tds = ''.join('<td class="%s">%s</td>'
                      % ('off' if v in ('휴진', '휴무', '-') else ('hi' if v.startswith('*') else ''),
                         v.lstrip('*'))
                      for v in r[1:])
        tr += '<tr><th>%s</th>%s</tr>' % (r[0], tds)
    inner = ('<table class="hours"><thead><tr><th></th>%s</tr></thead><tbody>%s</tbody></table>' % (th, tr))
    if note:
        inner += '<div class="notice" style="margin-top:16px"><p>%s</p></div>' % note
    return _wrap(sid, alt, eb, h2, sub, inner)


def badges(sid, alt, eb, h2, sub, items, note=''):
    b = ''.join('<span><i>◆</i>%s</span>' % x for x in items)
    inner = '<div class="badges">%s</div>' % b
    if note:
        inner += '<div class="notice" style="margin-top:20px"><p>%s</p></div>' % note
    return _wrap(sid, alt, eb, h2, sub, inner)


def dashboard(t):
    """관리자 화면 견본 — 다른 데모와 달리 옆에 메뉴가 붙는 구조입니다."""
    side = ''
    for grp, items in t['side']:
        side += '<div class="grp">%s</div>' % grp
        for name, on in items:
            side += '<a href="#" class="%s"><u></u>%s</a>' % ('on' if on else '', name)
    stat = ''.join(
        '<div class="s"><span>%s</span><b>%s</b><i>%s</i></div>' % (a, b, c)
        for a, b, c in t['stats'])
    rows = ''.join(
        '<tr>%s<td><span class="pill %s">%s</span></td></tr>'
        % (''.join('<td>%s</td>' % c for c in r[:-2]), r[-2], r[-1])
        for r in t['rows'])
    th = ''.join('<th>%s</th>' % c for c in t['cols'])
    return """
<div class="dash">
  <aside class="dside">
    <span class="lg">%s<i>.</i></span>
    %s
  </aside>
  <main class="dmain">
    <div class="dtop">
      <h1>%s</h1>
      <div class="sp"><a class="tb o" href="#">내보내기</a><a class="tb p" href="#">새로 쓰기</a></div>
    </div>
    <div class="stat">%s</div>
    <div class="dpanel">
      <div class="ph"><b>%s</b><span>%s</span></div>
      <table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>
    </div>
  </main>
</div>
"""% (t['brand'], side, t['dash_h1'], stat, t['panel'], t['panel_note'], th, rows)


# ── 사진이 없어서 그림은 SVG 로 그립니다 ────────────────────────────────
def art(kind, c1, c2):
    if kind == 'board':
        inner = ('<rect x="14" y="16" width="172" height="16" rx="4" fill="%s" opacity=".5"/>'
                 '<rect x="14" y="44" width="120" height="10" rx="3" fill="%s" opacity=".28"/>'
                 '<rect x="14" y="62" width="150" height="10" rx="3" fill="%s" opacity=".18"/>'
                 '<rect x="14" y="92" width="52" height="40" rx="6" fill="%s" opacity=".22"/>'
                 '<rect x="74" y="92" width="52" height="40" rx="6" fill="%s" opacity=".16"/>'
                 '<rect x="134" y="92" width="52" height="40" rx="6" fill="%s" opacity=".10"/>') % ((c1,) * 6)
    elif kind == 'cal':
        cells = ''
        for r in range(3):
            for k in range(4):
                on = (r == 1 and k == 2)
                cells += '<rect x="%d" y="%d" width="38" height="24" rx="5" fill="%s" opacity="%s"/>' % (
                    14 + k * 44, 40 + r * 32, c1, '.62' if on else '.13')
        inner = '<rect x="14" y="14" width="80" height="12" rx="4" fill="%s" opacity=".45"/>' % c1 + cells
    else:  # pulse
        inner = ('<circle cx="100" cy="74" r="46" fill="%s" opacity=".14"/>'
                 '<circle cx="100" cy="74" r="28" fill="%s" opacity=".24"/>'
                 '<path d="M40 74 h26 l10 -22 l14 44 l12 -30 l10 8 h48" fill="none" '
                 'stroke="%s" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>') % (c1, c1, c1)
    return ('<svg viewBox="0 0 200 148" width="100%%" height="100%%" aria-hidden="true" '
            'style="background:%s">%s</svg>' % (c2, inner))


TEMPLATES = [
    dict(
        file='academy.html', label='학원 · 교육',
        title='한빛어학원', brand='한빛어학원',
        desc='학원 홈페이지 참고 디자인 — 강사·커리큘럼 소개, 시간표, 상담 신청.',
        css="--t-accent:#1F62E0;--t-bg2:#F3F6FC;"
            "--t-head:'IBM Plex Sans KR',system-ui,sans-serif;",
        gfont='IBM+Plex+Sans+KR:wght@300;400;500;600;700',
        nav=[('s1', '수업안내'), ('s2', '강사진'), ('s3', '시간표')],
        cta='상담 신청', cta2='수업 먼저 보기',
        eb='신촌 · 성인 영어',
        h1='한 반 6명.<br>말할 차례가 돌아옵니다.',
        lead='레벨을 나눠 같은 수준끼리 묶습니다. 첫 수업 전에 배치 상담을 먼저 합니다.',
        photo='../media/tpl/academy-hero.jpg',
        stats=[('6','명','한 반 정원'),('4','단계','레벨 배치'),('92','%','재등록률'),('주 3','회','수업')],
        art=art('board', '#1F62E0', '#F3F6FC'),
        apply_eb='상담 신청', apply_h2='배치 상담부터 받아보세요.',
        apply_sub='지금 실력과 목표를 듣고 반을 정합니다.',
        apply_label='희망 과정',
        apply_opts=['기초 회화', '비즈니스 영어', '시험 대비', '아직 못 정했습니다'],
        foot='서울 서대문구 · 평일 10:00–22:00',
        body=[
            ('pcards', 's1', False, '수업 안내', '목표에 맞게 반을 나눕니다.', '레벨 배치 후 같은 수준끼리 수업합니다.',
             [('LEVEL 1-2', '기초 회화', '문장을 만드는 것부터. 말할 시간을 가장 많이 씁니다.', '../media/tpl/academy-a.jpg'),
              ('LEVEL 3', '비즈니스 영어', '회의·메일·발표에서 쓰는 표현을 다룹니다.', '../media/tpl/academy-b.jpg'),
              ('LEVEL 4', '시험 대비', '목표 점수와 남은 기간을 먼저 정하고 시작합니다.', None)]),
            ('spec', 's4', True, '레벨 안내', '지금 어디쯤인지 먼저 봅니다.', '배치 상담에서 레벨을 정하고 시작합니다.',
             [('레벨 1 · 입문', '단어는 아는데 문장이 안 나오는 단계. <em>현재-과거-미래</em> 세 시제로 말하는 것까지. 보통 3~4개월'),
              ('레벨 2 · 기초 회화', '짧게는 말하는데 길어지면 끊기는 단계. <em>이유·조건·비교</em>를 붙여 말합니다. 보통 4~6개월'),
              ('레벨 3 · 비즈니스', '일상은 되는데 업무에서 막히는 단계. <em>회의·메일·발표</em> 표현을 다룹니다. 보통 6개월'),
              ('레벨 4 · 시험 대비', '토익·오픽·토스. <em>목표 점수와 남은 기간</em>을 먼저 정하고 역산해서 짭니다.')]),
            ('hours', 's3', False, '시간표', '요일과 시간.', '정원이 차면 대기로 넘어갑니다.',
             ['월', '화', '수', '목', '금', '토'],
             [['07:00', '-', '*비즈니스', '-', '*비즈니스', '-', '-'],
              ['10:00', '-', '-', '-', '-', '-', '*시험 대비'],
              ['19:30', '*기초 회화', '-', '*기초 회화', '-', '*기초 회화', '-'],
              ['21:00', '*입문', '입문', '*입문', '입문', '*입문', '-']],
             '<b>한 반 6명</b>이라 정원이 금방 찹니다. 원하시는 시간이 마감이면 대기 걸어 드리고, '
             '자리가 나면 문자로 알려드립니다. 아침반은 출근 전에 듣는 분들이 많습니다.'),
            ('people', 's2', True, '강사진', '수업을 맡는 사람들.', '전임 강사가 같은 반을 끝까지 맡습니다. 강사가 중간에 바뀌지 않습니다.',
             [('김지훈', '회화 · 8년 · 캐나다 5년 거주'),
              ('박서연', '비즈니스 · 6년 · 前 외국계 마케팅'),
              ('이도현', '시험 대비 · 10년 · 토익 만점')]),
            ('spec', 's5', False, '수강료', '먼저 알려드립니다.', '교재비 외에 따로 받는 돈은 없습니다.',
             [('기초 회화 · 입문', '<em>주 3회 · 월 24만원</em> · 1회 90분'),
              ('비즈니스 영어', '<em>주 2회 · 월 20만원</em> · 1회 90분 · 아침반'),
              ('시험 대비', '<em>주 1회 · 월 16만원</em> · 1회 180분'),
              ('1:1 수업', '<em>회당 6만원</em> · 시간 협의'),
              ('교재비', '과정당 <em>2만원 안팎</em> · 실비'),
              ('환불', '학원법 기준 · 남은 횟수만큼 <em>일할 계산</em>')]),
            ('faq', 's6', True, '자주 묻는 질문', '', '',
             [('영어를 아예 못하는데 괜찮을까요',
               '입문반이 그 단계를 위한 반입니다. 배치 상담에서 지금 수준을 보고 시작점을 정하니 미리 준비하실 것은 없습니다.'),
              ('한 반에 몇 명인가요',
               '6명입니다. 90분 수업에서 한 사람이 말하는 시간을 확보하려면 이보다 많으면 안 된다고 봅니다.'),
              ('중간에 반을 바꿀 수 있나요',
               '가능합니다. 한 달쯤 들어보시고 너무 쉽거나 어려우면 강사와 상의해 옮깁니다. 추가 비용은 없습니다.'),
              ('결석하면 보강이 되나요',
               '월 1회까지 다른 반에서 보강하실 수 있습니다. 미리 말씀해 주시면 자리를 잡아 둡니다.'),
              ('원어민 수업인가요',
               '아닙니다. 문법과 표현을 한국어로 설명해야 하는 단계가 있어서, 전임 한국인 강사가 맡습니다. 레벨 3부터 원어민 대화 시간이 붙습니다.')]),
        ]),

    dict(
        file='clinic.html', label='병의원 · 치과',
        title='밝은미소치과', brand='밝은미소치과',
        desc='병의원 홈페이지 참고 디자인 — 진료과목, 의료진, 진료시간, 예약.',
        css="--t-accent:#0FA3A3;--t-bg2:#F1F8F8;--t-round:14px;"
            "--t-title:'Gowun Dodum',system-ui,sans-serif;",
        gfont='Gowun+Dodum', align='al-c',
        nav=[('s1', '진료과목'), ('s2', '의료진'), ('s3', '진료시간')],
        cta='예약 문의', cta2='진료과목 보기',
        eb='신촌역 2번 출구',
        h1='아프기 전에<br>한 번 더 봅니다.',
        lead='치료보다 예방을 먼저 말씀드립니다. 필요 없는 치료는 권하지 않습니다.',
        photo='../media/tpl/clinic-hero.jpg',
        stats=[('14','년','원장 진료 경력'),('4','대','진료 유닛'),('09:30','~','평일 진료 시작'),('토','요일','오전 진료')],
        art=art('pulse', '#0FA3A3', '#F1F8F8'),
        apply_eb='예약 문의', apply_h2='진료 예약을 남겨주세요.',
        apply_sub='확인 후 연락드려 시간을 확정합니다.',
        apply_label='진료 희망',
        apply_opts=['일반 검진', '충치 치료', '교정 상담', '임플란트 상담'],
        foot='서울 서대문구 · 평일 09:30–18:30 / 토 09:30–13:00',
        body=[
            ('pcards', 's1', False, '진료과목', '무엇을 보는 곳인가.', '과잉 진료를 하지 않는 것을 원칙으로 합니다.',
             [('GENERAL', '일반 진료', '충치, 잇몸, 사랑니. 먼저 상태부터 설명드립니다.', '../media/tpl/clinic-a.jpg'),
              ('ORTHO', '교정', '시작 전에 기간과 비용을 모두 알려드립니다.', '../media/tpl/clinic-b.jpg'),
              ('CHECK-UP', '정기 검진', '6개월에 한 번, 문자로 알려드립니다.', None)]),
            ('steps4', 's4', True, '진료 절차', '오시면 이렇게 진행됩니다.', '처음 오신 분은 30분 정도 걸립니다.',
             [('접수 · 문진', '어디가 불편한지, 지금까지 어떤 치료를 받으셨는지 여쭙습니다.', '5분'),
              ('검사', '파노라마 엑스레이를 찍고 구강 상태를 봅니다. 필요하면 3D 촬영을 합니다.', '10분'),
              ('설명 · 상담', '찍은 사진을 화면에 띄워 같이 보면서 설명드립니다. 치료 안 해도 되는 것은 안 한다고 말씀드립니다.', '10분'),
              ('치료 계획', '기간과 비용을 종이에 적어 드립니다. 그날 결정하지 않으셔도 됩니다.', '5분')]),
            ('hours', 's3', False, '진료시간', '언제 여나요.', '일요일·공휴일은 쉽니다.',
             ['월', '화', '수', '목', '금', '토'],
             [['오전', '09:30–13:00', '09:30–13:00', '09:30–13:00', '09:30–13:00', '09:30–13:00', '*09:30–13:00'],
              ['오후', '14:00–18:30', '14:00–18:30', '*14:00–21:00', '14:00–18:30', '14:00–18:30', '휴진']],
             '<b>수요일은 밤 9시까지</b> 봅니다. 직장 다니시는 분들을 위해 열어 두었습니다. '
             '토요일은 점심시간 없이 오전만 진료합니다. 점심시간은 평일 13:00–14:00 입니다.'),
            ('people', 's2', True, '의료진', '진료를 맡는 사람들.', '수납·상담·치료를 같은 사람이 끝까지 봅니다.',
             [('원장 정민호', '보존과 전문의 · 14년'), ('부원장 한수아', '교정과 전문의 · 9년'), ('실장 오지은', '상담 · 11년')]),
            ('spec', 's5', False, '비용 안내', '자주 묻는 항목만 적었습니다.', '건강보험이 안 되는 항목은 따로 표시했습니다.',
             [('레진 (충치 1개)', '<em>10만 ~ 15만원</em> · 비급여 · 충치 크기에 따라 다릅니다'),
              ('신경치료', '<em>보험 적용</em> · 본인부담금 3만원 안팎 · 치아 위치에 따라 다릅니다'),
              ('크라운 (지르코니아)', '<em>45만 ~ 60만원</em> · 비급여'),
              ('임플란트 (1개)', '<em>90만 ~ 140만원</em> · 비급여 · 뼈 상태에 따라 뼈이식이 추가될 수 있습니다'),
              ('스케일링', '<em>보험 적용</em> · 연 1회 · 본인부담금 1만 5천원 안팎'),
              ('교정 상담', '<em>무료</em> · 검사비는 별도입니다')]),
            ('faq', 's6', True, '자주 묻는 질문', '오시기 전에 많이 물어보시는 것.', '',
             [('처음인데 뭘 가져가야 하나요',
               '신분증만 가져오시면 됩니다. 다른 병원에서 찍은 엑스레이가 있으면 가져오시면 다시 안 찍어도 됩니다.'),
              ('예약 없이 가도 되나요',
               '가능합니다. 다만 예약하신 분이 먼저라 기다리실 수 있습니다. 전화로 오시는 시간만 알려주셔도 대기가 줄어듭니다.'),
              ('치료비를 한 번에 못 내면 어떻게 하나요',
               '임플란트·교정처럼 금액이 큰 치료는 치료 단계에 맞춰 나눠 내실 수 있습니다. 카드 무이자 할부도 됩니다.'),
              ('아이도 볼 수 있나요',
               '만 6세부터 봅니다. 불소도포와 실런트는 보험이 됩니다.'),
              ('주차되나요',
               '건물 지하에 대실 수 있고 2시간 무료입니다. 진료 끝나고 데스크에 주차권을 말씀해 주세요.')]),
        ]),

    dict(
        file='counsel.html', label='상담 · 심리',
        title='담온심리상담센터', brand='담온상담센터',
        desc='심리상담센터 홈페이지 참고 디자인 — 상담 안내, 상담사 소개, 신청.',
        css="--t-accent:#5E7C8C;--t-bg2:#F5F2EC;--t-ink:#24313A;--t-round:6px;"
            "--t-title:'Gowun Batang',serif;",
        gfont='Gowun+Batang:wght@400;700', align='al-r',
        nav=[('s1', '상담안내'), ('s2', '상담사'), ('s3', '비용')],
        cta='상담 신청', cta2='상담 안내 보기',
        eb='성인 개인 상담',
        h1='말이 정리되지 않아도<br>괜찮습니다.',
        lead='무엇부터 말해야 할지 모르는 채로 오셔도 됩니다. 그 지점부터 함께 봅니다.',
        stats=[('50','분','1회 상담'),('12','년','최다 경력'),('3','명','상담사'),('예약','제','운영')],
        art=art('board', '#5E7C8C', '#F5F2EC'),
        apply_eb='상담 신청', apply_h2='첫 상담을 신청하세요.',
        apply_sub='적어주신 내용은 상담자만 봅니다.',
        apply_label='상담 방식',
        apply_opts=['대면 상담', '화상 상담', '아직 못 정했습니다'],
        foot='서울 서대문구 · 예약제 운영',
        body=[
            ('cards', 's1', False, '상담 안내', '어떻게 진행되나.', '첫 상담에서 방향을 함께 정합니다.',
             [('개인 상담', '1회 50분. 정기적으로 만나며 흐름을 봅니다.'),
              ('첫 상담', '지금 가장 힘든 것과 다루고 싶은 것을 정리합니다.'),
              ('화상 상담', '오기 어려운 경우 화면으로 진행합니다.')], 'g3'),
            ('steps4', 's4', True, '상담은 이렇게 흘러갑니다', '처음 오시는 분이 가장 궁금해하시는 것.',
             '몇 회에 끝난다고 미리 정하지 않습니다. 다만 대개 이런 흐름입니다.',
             [('첫 상담', '지금 무엇이 가장 힘든지 듣습니다. 정리해서 말씀하지 않으셔도 됩니다.', '1회'),
              ('방향 정하기', '무엇을 다룰지 함께 정합니다. 목표가 분명해야 끝이 보입니다.', '2~3회'),
              ('탐색', '반복되는 감정과 관계 패턴이 어디서 왔는지 봅니다. 여기가 가장 깁니다.', '8~15회'),
              ('마무리', '달라진 것을 정리하고, 혼자서도 돌볼 수 있는지 확인합니다.', '2회')]),
            ('people', 's2', False, '상담사', '만나게 될 사람.', '자격증 번호는 상담 때 직접 보여드립니다.',
             [('윤가온', '임상심리전문가 · 12년'),
              ('서지후', '상담심리사 1급 · 8년'),
              ('노하린', '미술치료사 1급 · 7년')]),
            ('spec', 's3', True, '비용', '미리 알려드립니다.', '상담 중에 추가로 드는 비용은 없습니다.',
             [('첫 상담', '<em>60,000원</em> · 50분 · 이후 계속할지는 그때 정하셔도 됩니다'),
              ('개인 상담', '<em>80,000원</em> · 50분 · 보통 주 1회'),
              ('부부 · 가족 상담', '<em>110,000원</em> · 80분'),
              ('심리검사', '<em>150,000원</em> · 검사 1회 + 해석 상담 1회 · MMPI, 기질검사 등'),
              ('미술치료', '<em>80,000원</em> · 50분 · 재료비 포함'),
              ('취소', '<em>24시간 전</em>까지 말씀해 주시면 비용이 발생하지 않습니다')]),
            ('faq', 's5', False, '자주 묻는 질문', '', '',
             [('무슨 말부터 해야 할지 모르겠어요',
               '그 상태로 오셔도 됩니다. 무엇부터 말해야 할지 모르겠다는 것 자체가 첫 상담의 시작점이 됩니다.'),
              ('몇 번이나 와야 하나요',
               '미리 정하지 않습니다. 다만 한두 번으로 달라지기는 어렵고, 대개 10회 안팎에서 변화를 느끼십니다. 언제든 그만두실 수 있습니다.'),
              ('상담 내용이 밖으로 나가지 않나요',
               '나가지 않습니다. 상담자에게는 비밀유지 의무가 있습니다. 다만 자신이나 타인의 생명이 위험한 경우처럼 법이 정한 예외는 첫 상담에서 미리 설명드립니다.'),
              ('약을 먹고 있는데 상담을 같이 받아도 되나요',
               '됩니다. 다니시는 병원이 있으면 알려주세요. 약물 치료와 상담은 서로 다른 역할을 합니다.'),
              ('가족이 받았으면 하는데 본인이 싫다고 해요',
               '억지로 데려오시면 상담이 잘 되지 않습니다. 대신 가족분이 먼저 오셔서 어떻게 대하면 좋을지 상의하는 경우가 많습니다.')]),
        ]),

    dict(
        file='company.html', label='기업 · 기관',
        title='대한정밀', brand='대한정밀',
        desc='기업·기관 홈페이지 참고 디자인 — 회사소개, 사업분야, 연혁, 조직.',
        css="--t-accent:#111418;--t-bg2:#F2F3F5;--t-round:0px;"
            "--t-title:'Black Han Sans',sans-serif;",
        gfont='Black+Han+Sans', align='al-tl',
        photo='../media/tpl/company-hero.jpg',
        stats=[('1996','~','설립'),('±0.005','mm','대응 공차'),('5','축','가공기'),('ISO','9001','인증')],
        nav=[('s1', '사업분야'), ('s2', '연혁'), ('s3', '조직')],
        cta='문의하기', cta2='사업분야 보기',
        eb='ESTABLISHED 1996',
        h1='정밀가공,<br>30년의 공차.',
        lead='자동차·반도체 장비 부품을 만듭니다. 도면 검토부터 양산까지 한 곳에서 진행합니다.',
        art=art('cal', '#111418', '#F2F3F5'),
        apply_eb='문의', apply_h2='도면을 보내주세요.',
        apply_sub='검토 후 가능 여부와 일정을 회신드립니다.',
        apply_label='문의 구분',
        apply_opts=['견적 문의', '기술 협의', '채용 문의', '기타'],
        foot='경기도 화성시 · 평일 08:30–17:30',
        body=[
            ('pcards', 's1', False, '사업분야', '무엇을 만드나.', '소량 시작품부터 양산까지 대응합니다.',
             [('MACHINING', '정밀 절삭', '5축 가공. 공차 ±0.005mm 까지 대응합니다.', '../media/tpl/company-a.jpg'),
              ('MOLD', '금형 제작', '설계부터 시험사출까지 사내에서 처리합니다.', '../media/tpl/company-b.jpg'),
              ('QC', '조립 · 검사', '전수 검사 후 성적서와 함께 납품합니다.', None)]),
            ('spec', 's4', True, '보유 설비', '무엇으로 만드나.', '도면을 보내주시면 어느 장비로 가능한지 회신드립니다.',
             [('5축 가공기', 'DMG MORI DMU 50 <em>2대</em> · 최대 가공 500×450×400mm · 공차 ±0.005mm'),
              ('CNC 선반', 'DOOSAN PUMA 2600 <em>4대</em> · 최대 척 250mm · 봉재 자동공급'),
              ('머시닝센터', 'HYUNDAI WIA F500 <em>6대</em> · 3축 · 대량 양산용'),
              ('와이어 방전', 'Sodick AQ537L <em>1대</em> · 금형 코어 가공'),
              ('3차원 측정기', 'Mitutoyo CRYSTA-Apex <em>2대</em> · 전수 검사 · 성적서 발행'),
              ('사출기', '100톤 ~ 250톤 <em>3대</em> · 시험사출 및 소량 양산')]),
            ('timeline', 's2', False, '연혁', '걸어온 길.', '주요 사항만 추렸습니다.',
             [('1996', '대한정밀 설립', '화성 향남에서 선반 2대로 시작했습니다.'),
              ('2004', '제1공장 준공', '자체 공장을 짓고 CNC 라인을 갖췄습니다. 자동차 부품 1차 협력사 등록.'),
              ('2013', 'ISO 9001 인증', '품질경영시스템을 도입하고 전수 검사 체계를 만들었습니다.'),
              ('2018', '반도체 장비 부품 진입', '±0.005mm 정밀 가공이 필요한 물량을 맡기 시작했습니다.'),
              ('2021', '5축 가공기 도입 · 제2공장 증설', '한 번 물려서 다섯 면을 가공합니다. 공정이 줄어 납기가 빨라졌습니다.'),
              ('2025', '누적 납품 1,200만 개', '불량률 0.02% 를 유지하고 있습니다.')]),
            ('badges', 's5', True, '인증 · 등록', '증빙이 필요하시면 사본을 보내드립니다.', '',
             ['ISO 9001:2015', '자동차부품 1차 협력사', '벤처기업 확인', '기업부설연구소',
              '뿌리기술 전문기업', '특허 4건 · 실용신안 2건'],
             '<b>도면 검토는 무료입니다.</b> 2D·3D 어느 쪽이든 보내주시면 가공 가능 여부, 예상 단가, '
             '납기를 <b>3일 안에</b> 회신드립니다. 보내주신 도면은 검토 후 폐기하며 외부에 공유하지 않습니다.'),
            ('steps4', 's3', False, '일하는 순서', '주문부터 납품까지.', '진행 상황은 담당자가 주 1회 알려드립니다.',
             [('도면 검토', '가공 가능한지, 더 싸게 만들 방법이 있는지 먼저 봅니다.', '3일'),
              ('견적 · 계약', '자재비와 가공비를 나눠 적은 견적서를 드립니다.', '2일'),
              ('시제품', '1~2개를 먼저 만들어 치수를 맞춰 보고 승인받습니다.', '1~2주'),
              ('양산 · 납품', '전수 검사 후 성적서와 함께 보냅니다.', '수량에 따라')]),
        ]),

    dict(
        file='law.html', label='법률 · 세무',
        title='정도법률사무소', brand='정도법률사무소',
        desc='법률·세무 사무소 홈페이지 참고 디자인 — 업무분야, 구성원, 상담 예약.',
        css="--t-accent:#8A6A3B;--t-bg2:#F7F5F1;--t-ink:#1C1A17;--t-round:2px;"
            "--t-title:'Nanum Myeongjo',serif;",
        gfont='Nanum+Myeongjo:wght@400;700;800', align='al-c',
        nav=[('s1', '업무분야'), ('s2', '구성원'), ('s3', '상담절차')],
        cta='상담 예약', cta2='업무분야 보기',
        eb='서울 서초 · 2009',
        h1='이길 수 있는 사건인지<br>먼저 말씀드립니다.',
        lead='가능성이 낮으면 낮다고 합니다. 착수 전에 예상 기간과 비용을 서면으로 드립니다.',
        stats=[('2009','~','개소'),('4','개','업무 분야'),('50','분','상담 시간'),('3','일','수임 회신')],
        art=art('board', '#8A6A3B', '#F7F5F1'),
        apply_eb='상담 예약', apply_h2='상담부터 잡아보세요.',
        apply_sub='사건 개요를 간단히 적어주시면 담당 변호사가 배정됩니다.',
        apply_label='사건 구분',
        apply_opts=['민사', '형사', '가사·이혼', '기업 자문', '아직 모르겠습니다'],
        foot='서울 서초구 · 평일 09:00–18:00',
        body=[
            ('cards', 's1', False, '업무분야', '주로 다루는 사건.', '분야를 넓히기보다 하던 것을 깊게 합니다.',
             [('민사 · 손해배상', '계약 분쟁, 대여금, 공사대금, 손해배상.'),
              ('형사', '수사 단계부터 함께합니다. 초기 대응이 결과를 가릅니다.'),
              ('가사 · 이혼', '재산분할과 양육을 중심으로 정리합니다.'),
              ('기업 자문', '계약서 검토, 노무, 지식재산 분쟁.')], 'g4'),
            ('cases', 's4', True, '맡았던 사건', '어떤 사건을 어떻게 풀었는지.',
             '의뢰인이 특정되지 않도록 사건 내용을 바꿔 적었습니다.',
             [('공사대금', '기성금을 못 받은 하도급 업체',
               '원청이 "하자가 있다"며 잔금 1억 8천을 미루던 사건입니다. 하자 주장이 근거가 있는지부터 감정으로 가렸습니다.',
               '전액 지급 판결<br>소요 11개월'),
              ('손해배상', '계약 해지 통보를 받은 대리점',
               '본사가 갱신을 거절하며 재고를 떠안긴 경우입니다. 거래 관행과 투자금 회수 여부를 다퉜습니다.',
               '조정 성립<br>재고 인수 + 보상금'),
              ('형사', '수사 초기 단계에서 상담 온 의뢰인',
               '고소장이 접수된 직후 오셨습니다. 조사 전에 사실관계를 정리하고 진술 방향을 잡았습니다.',
               '불송치 결정<br>소요 4개월'),
              ('가사', '재산분할이 쟁점이던 이혼',
               '혼인 기간 중 형성된 재산의 기여도를 다퉜습니다. 통장 내역과 대출 상환 기록을 시간순으로 정리했습니다.',
               '분할 비율 45%<br>양육권 확보'),
              ('기업 자문', '계약서 검토를 맡긴 제조업체',
               '납품 계약서에 손해배상 상한이 없어 위험이 컸습니다. 조항별로 위험을 표시해 드리고 대안을 넣었습니다.',
               '상한 조항 삽입<br>분쟁 없이 종료')]),
            ('spec', 's5', False, '수임료 안내', '먼저 말씀드립니다.', '사건마다 다르지만 기준은 이렇습니다.',
             [('상담료', '<em>5만원 / 50분</em> · 수임하시면 착수금에서 빼 드립니다'),
              ('민사 착수금', '<em>330만원부터</em> · 소가와 난이도에 따라 협의합니다'),
              ('성공보수', '<em>회수 금액의 10% 안팎</em> · 착수 전에 비율을 서면으로 정합니다'),
              ('형사 (수사 단계)', '<em>440만원부터</em> · 조사 동행 포함'),
              ('기업 자문 (월 고문)', '<em>월 55만원부터</em> · 계약서 검토 월 3건 포함'),
              ('인지대 · 송달료', '실비 · <em>의뢰인 부담</em> · 영수증을 그대로 드립니다')]),
            ('people', 's2', True, '구성원', '사건을 맡는 사람.', '수임한 변호사가 끝까지 직접 담당합니다. 사무장이 대신 맡지 않습니다.',
             [('대표변호사 조현우', '사법연수원 38기 · 민사 · 15년'),
              ('변호사 임세라', '변호사시험 5회 · 가사 · 8년'),
              ('세무사 백준영', '세무 · 12년 · 상속·양도 담당')]),
            ('steps4', 's3', False, '상담 절차', '이렇게 진행됩니다.', '상담료는 수임하시면 착수금에서 차감됩니다.',
             [('예약', '사건 개요를 간단히 남기시면 담당 변호사를 배정합니다.', '당일~2일'),
              ('자료 정리', '어떤 서류가 필요한지 미리 알려드립니다. 없어도 상담은 됩니다.', '-'),
              ('대면 상담', '가능성과 예상 기간을 솔직히 말씀드립니다. 어려우면 어렵다고 합니다.', '50분'),
              ('수임 결정', '착수금·성공보수·실비를 서면으로 드립니다. 그날 정하지 않으셔도 됩니다.', '3일 내')]),
            ('faq', 's6', True, '자주 묻는 질문', '', '',
             [('이길 수 있는 사건인지 미리 알 수 있나요',
               '상담 단계에서 가능성이 낮으면 낮다고 말씀드립니다. 승소를 장담하는 것은 변호사 광고 규정상으로도 할 수 없고, 저희는 하지 않습니다.'),
              ('소송까지 안 가고 끝낼 수 있나요',
               '내용증명이나 조정으로 끝나는 경우가 적지 않습니다. 소송은 시간과 비용이 크니 다른 방법부터 검토합니다.'),
              ('얼마나 걸리나요',
               '민사 1심은 보통 8개월에서 1년 반입니다. 상대가 다투는 정도와 감정 절차 유무에 따라 달라집니다.'),
              ('비용을 나눠 낼 수 있나요',
               '착수금은 분할이 가능합니다. 상담 때 말씀해 주세요.'),
              ('다른 변호사에게 맡겼던 사건도 되나요',
               '됩니다. 진행 중인 기록을 보고 이어받을지, 지금 방향이 맞는지부터 봅니다.')]),
        ]),

    dict(
        file='interior.html', label='부동산 · 인테리어',
        title='여백건축', brand='여백건축',
        desc='건축·인테리어 홈페이지 참고 디자인 — 시공 사례, 진행 과정, 견적 문의.',
        css="--t-accent:#C2410C;--t-bg2:#FAF7F4;--t-round:0px;"
            "--t-title:'Noto Serif KR',serif;",
        gfont='Noto+Serif+KR:wght@300;500;700', bare=True,
        nav=[('s1', '시공사례'), ('s2', '진행과정'), ('s3', '견적기준')],
        cta='견적 문의', cta2='사례 보기',
        eb='주거 · 상업 공간',
        h1='도면보다<br>사는 방식을 먼저 봅니다.',
        lead='평면부터 그리지 않습니다. 몇 시에 어디에 있는지를 듣고 그 다음에 벽을 세웁니다.',
        photo='../media/tpl/interior-hero.jpg',
        stats=[('120','건','시공 사례'),('4~8','주','평균 공기'),('1','년','하자 보수'),('주 1','회','현장 사진')],
        art=art('cal', '#C2410C', '#FAF7F4'),
        apply_eb='견적 문의', apply_h2='도면이나 사진을 보내주세요.',
        apply_sub='평수와 예산 범위만 알려주셔도 대략 잡아드립니다.',
        apply_label='공간 구분',
        apply_opts=['아파트', '단독주택', '상가·카페', '사무실'],
        foot='서울 마포구 · 평일 10:00–19:00',
        body=[
            ('pcards', 's1', False, '시공 사례', '해온 일.', '사진은 보정 없이 그대로 올립니다.',
             [('APARTMENT', '연희동 32평', '벽을 하나 트고 창을 키웠습니다.', '../media/tpl/interior-a.jpg'),
              ('HOUSE', '일산 단독주택', '단열과 창호부터 다시 했습니다.', '../media/tpl/interior-b.jpg'),
              ('CAFE', '망원 상가 카페', '주방 동선을 먼저 잡고 객석을 배치했습니다.', None)]),
            ('cases', 's4', True, '해온 일', '언제, 어디를, 얼마에.',
             '금액은 그 당시 기준이라 지금과 다를 수 있습니다.',
             [('아파트 32평', '연희동 · 벽을 하나 트고 창을 키웠습니다',
               '거실과 방 사이 비내력벽을 철거해 하나로 이었습니다. 남향 창을 넓히고 단열을 다시 했습니다. 주방 동선을 ㄱ자로 바꿨습니다.',
               '공사 6주<br>4,800만원'),
              ('단독주택', '일산 · 단열과 창호부터 다시 했습니다',
               '20년 된 집이라 겉보다 속이 문제였습니다. 외벽 단열재를 새로 넣고 창을 3중으로 바꾼 뒤에 마감을 했습니다.',
               '공사 9주<br>1억 1,200만원'),
              ('상가 카페', '망원 · 주방 동선을 먼저 잡았습니다',
               '객석부터 그리면 주방이 좁아집니다. 반대로 했습니다. 전기 용량과 배수를 먼저 확인해 설비를 앉혔습니다.',
               '공사 5주<br>6,300만원'),
              ('사무실', '성수 · 회의실만 새로 만들었습니다',
               '전체를 안 건드리고 유리 파티션으로 회의실 두 개를 냈습니다. 소음이 문제라 흡음재를 넣었습니다.',
               '공사 3주<br>2,100만원')]),
            ('steps4', 's2', False, '진행 과정', '얼마나 걸리나.', '착공하면 매주 현장 사진을 보내드립니다.',
             [('현장 실측', '직접 가서 치수를 재고 상태를 봅니다. 배관·전기·단열은 눈에 안 보여서 이때 확인해야 합니다.', '1일'),
              ('설계 · 견적', '도면을 그리고 자재를 골라 금액을 확정합니다. 이 단계에서 바꾸는 것은 돈이 안 듭니다.', '2주'),
              ('시공', '철거 → 설비·전기 → 목공 → 마감 순으로 갑니다. 공정마다 확인받고 넘어갑니다.', '3~9주'),
              ('입주 · 보수', '청소 후 같이 돌아보며 확인합니다. 이후 1년간 하자 보수를 합니다.', '1년')]),
            ('spec', 's3', True, '견적 기준', '돈이 어디에 드는지 나눠 적습니다.', '뭉뚱그린 "평당 얼마" 로 드리지 않습니다.',
             [('철거 · 폐기물', '<em>평당 8~15만원</em> · 벽을 트는지, 바닥을 걷어내는지에 따라 다릅니다'),
              ('설비 · 전기', '<em>400~900만원</em> · 배관 교체 여부가 가장 큽니다'),
              ('목공 · 도장', '<em>평당 25~45만원</em> · 붙박이장과 몰딩 범위에 따라'),
              ('바닥재', '강마루 <em>평당 12만원</em> / 원목마루 <em>평당 28만원</em>부터'),
              ('창호', '3중 시스템창 <em>개당 90~180만원</em> · 단열 성능에 따라'),
              ('설계비', '<em>총 공사비의 5%</em> · 시공을 맡기시면 공사비에서 빼 드립니다')]),
            ('faq', 's5', False, '자주 묻는 질문', '', '',
             [('예산을 얼마나 잡아야 하나요',
               '32평 아파트 전체를 손보면 4,000만원 안팎에서 시작합니다. 부분만 하시면 훨씬 적게 듭니다. 예산을 먼저 말씀해 주시면 그 안에서 무엇을 할 수 있는지 정리해 드립니다.'),
              ('살면서 공사할 수 있나요',
               '부분 공사는 가능합니다. 다만 철거와 도장이 들어가면 먼지와 냄새 때문에 권하지 않습니다. 그 기간만 나가 계시는 것이 낫습니다.'),
              ('공사 중에 금액이 늘어나지 않나요',
               '뜯어보고 나서야 아는 것들이 있습니다(누수, 배관 부식 등). 그럴 때는 먼저 사진으로 알려드리고 동의를 받은 뒤에 진행합니다. 말없이 더하지 않습니다.'),
              ('하자가 생기면요',
               '입주 후 1년간 무상으로 봐 드립니다. 연락 주시면 3일 안에 가서 확인합니다.'),
              ('자재를 직접 고를 수 있나요',
               '고르셔도 됩니다. 다만 시공이 어려운 자재는 미리 말씀드립니다. 저희가 쓰는 브랜드와 등급은 견적서에 그대로 적습니다.')]),
        ]),
]


def build():
    made = []
    for t in TEMPLATES:
        if t.get('kind') == 'dash':
            html = head(t) + dashboard(t) + footer(t)
            with io.open(os.path.join(HERE, t['file']), 'w', encoding='utf-8', newline='\r\n') as f:
                f.write(html)
            made.append((t['file'], t['label'], len(html)))
            continue
        parts = [head(t), header(t), phero(t)]
        if t.get('stats'): parts.append(statbar(t['stats']))
        for b in t['body']:
            kind = b[0]
            if kind == 'cards':
                parts.append(cards(b[1], b[2], b[3], b[4], b[5], b[6], b[7]))
            elif kind == 'table':
                parts.append(table(b[1], b[2], b[3], b[4], b[5], b[6], b[7]))
            elif kind == 'people':
                parts.append(people(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'pcards':
                parts.append(pcards(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'steps4':
                parts.append(steps4(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'spec':
                parts.append(spec(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'timeline':
                parts.append(timeline(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'cases':
                parts.append(cases(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'faq':
                parts.append(faq(b[1], b[2], b[3], b[4], b[5], b[6]))
            elif kind == 'hours':
                parts.append(hours(b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8] if len(b) > 8 else ''))
            elif kind == 'badges':
                parts.append(badges(b[1], b[2], b[3], b[4], b[5], b[6], b[7] if len(b) > 7 else ''))
        parts.append(apply_sec(t))
        parts.append(footer(t))
        html = ''.join(parts)
        with io.open(os.path.join(HERE, t['file']), 'w', encoding='utf-8', newline='\r\n') as f:
            f.write(html)
        made.append((t['file'], t['label'], len(html)))
    for f, l, n in made:
        print('%-16s %-14s %6d bytes' % (f, l, n))


if __name__ == '__main__':
    build()
