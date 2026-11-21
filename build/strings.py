# ポートフォリオの文言（英・日・仏）。ここだけ直せば 3 つのページが一緒に変わる。
# 書き出し： python3 build/build.py
S = {
"lang": {"en": "en", "ja": "ja", "fr": "fr"},
"title": {"en": "Kentaro Maeda — Video Editor", "ja": "前田健太郎 — 映像編集", "fr": "Kentaro Maeda — Monteur vidéo"},
"desc": {
 "en": "Kentaro Maeda, video editor in Kamakura, Japan. Live action, motion, and AI-assisted pipelines that turn one script into every format.",
 "ja": "鎌倉の映像編集者、前田健太郎。実写・モーション、そして台本1枚からすべての形式を書き出すAIのワークフロー。",
 "fr": "Kentaro Maeda, monteur vidéo à Kamakura. Prises de vue réelles, motion design et outils d’IA qui déclinent un seul script dans tous les formats."},
"brand": {"en": "Kentaro Maeda", "ja": "前田健太郎", "fr": "Kentaro Maeda"},
"nav_work": {"en": "Work", "ja": "作品", "fr": "Projets"},
"nav_process": {"en": "Process", "ja": "進め方", "fr": "Méthode"},
"nav_about": {"en": "About", "ja": "経歴", "fr": "Parcours"},
"nav_contact": {"en": "Contact", "ja": "連絡先", "fr": "Contact"},

"kicker": {"en": "Video editor · Kamakura, Japan", "ja": "映像編集 · 神奈川県鎌倉市", "fr": "Monteur vidéo · Kamakura, Japon"},
"h1": {
 "en": "I cut for <em>timing</em>, and build the tools that make it fast.",
 "ja": "<em>間</em>で切る。<br>そのための道具も、<br>自分でつくる。",
 "fr": "Je monte au <em>tempo</em>, et je construis les outils qui vont avec."},
"lead": {
 "en": "Live action, motion and short-form. Five years producing client videos end to end, twenty years on stage as a dancer, and AI-assisted pipelines that turn one script into every format.",
 "ja": "実写、モーション、ショート動画。企業のPR映像を企画から納品まで5年、ダンサーとして舞台に立って20年。台本1枚から全部の形式を書き出す、AIを使った制作の仕組みも自分で組んでいます。",
 "fr": "Prises de vue réelles, motion design et formats courts. Cinq ans à produire des vidéos pour des clients de A à Z, vingt ans sur scène comme danseur, et des outils d’IA qui déclinent un seul script dans tous les formats."},
"chip1": {"en": "Remote · JST (UTC+9)", "ja": "リモート · 日本時間", "fr": "À distance · JST (UTC+9)"},
"chip2": {"en": "DaVinci Resolve · Remotion · Python", "ja": "DaVinci Resolve · Remotion · Python", "fr": "DaVinci Resolve · Remotion · Python"},
"chip3": {"en": "Japanese · English · French", "ja": "日本語 · 英語 · フランス語", "fr": "Japonais · anglais · français"},

# 01
"w1_kicker": {"en": "01 · Developer explainer · spec piece", "ja": "01 · 技術解説動画 · 自主制作", "fr": "01 · Vidéo explicative tech · projet personnel"},
"w1_title": {"en": "Why one database hits a wall", "ja": "なぜ1台のデータベースは限界を迎えるのか", "fr": "Pourquoi une seule base de données finit par saturer"},
"w1_note": {"en": "", "ja": "動画は英語です。", "fr": "La vidéo est en anglais."},
"source": {"en": "Source on GitHub ↗", "ja": "GitHubでコードを見る ↗", "fr": "Code source sur GitHub ↗"},
"k_format": {"en": "Format", "ja": "形式", "fr": "Format"},
"k_role": {"en": "Role", "ja": "担当", "fr": "Rôle"},
"k_built": {"en": "Built with", "ja": "使った道具", "fr": "Outils"},
"k_speed": {"en": "Speed", "ja": "速さ", "fr": "Rapidité"},
"k_source": {"en": "Source", "ja": "素材", "fr": "Rushes"},
"w1_format": {"en": "66 s, 16:9 · 35 s vertical cut · 2 thumbnails", "ja": "66秒・横 · 35秒の縦型 · サムネイル2案", "fr": "66 s en 16:9 · version verticale de 35 s · 2 vignettes"},
"w1_role": {"en": "Script, motion, sound, edit", "ja": "台本・動き・音・編集", "fr": "Script, animation, son, montage"},
"w1_built": {"en": "Remotion, Kokoro TTS, Whisper, Python, Claude", "ja": "Remotion、Kokoro TTS、Whisper、Python、Claude", "fr": "Remotion, Kokoro TTS, Whisper, Python, Claude"},
"w1_speed": {
 "en": "First full cut in ~40 min. One script line changed, re-voiced and re-timed in 2 min 26 s",
 "ja": "初稿まで約40分。台本1行の変更から、声・字幕・タイミングの作り直しまで2分26秒",
 "fr": "Premier montage complet en ~40 min. Une ligne du script modifiée, revoisée et recalée en 2 min 26 s"},
"decisions": {"en": "Decisions", "ja": "判断したこと", "fr": "Choix"},
"w1_d1": {
 "en": "Subject on screen in the first second: “1 database.” A frame check caught it arriving at 2.2 s, so it moved to 0.45 s.",
 "ja": "最初の1秒で主題を出す。静止画で確認したら「1 database.」が2.2秒まで出ていなかったので、0.45秒に早めた。",
 "fr": "Le sujet à l’écran dès la première seconde : « 1 database. » Une vérification image par image l’a vu arriver à 2,2 s ; il passe à 0,45 s."},
"w1_d2": {
 "en": "Picture and sound read one cue sheet, so the database splits on the word “split”, with the sound.",
 "ja": "画と音が同じ時刻表を見るので、「split」と言った瞬間にデータベースが割れ、音も鳴る。",
 "fr": "Image et son lisent la même feuille de repères : la base se divise sur le mot « split », avec le son."},
"w1_d3": {
 "en": "Narration is re-transcribed by Whisper to catch mispronunciations and to time captions word by word.",
 "ja": "ナレーションはWhisperで聞き直して読み間違いを見つけ、字幕も1語ずつのタイミングに合わせる。",
 "fr": "La voix off est retranscrite par Whisper pour repérer les erreurs de prononciation et caler les sous-titres mot à mot."},
"cap_short": {"en": "Vertical cut, generated from the same source.", "ja": "縦型ショート。同じ元原稿から自動で書き出し。", "fr": "Version verticale, générée à partir de la même source."},
"cap_making": {
 "en": "Making-of: the pipeline, a one-line change before/after, machine QA, fixes caught on stills.",
 "ja": "メイキング：制作の流れ、台本1行の変更の前後、機械での検品、静止画で見つけた修正。",
 "fr": "Making-of : la chaîne de production, une ligne modifiée avant/après, le contrôle automatique, les corrections repérées image par image."},
"spec": {
 "en": "Spec piece made for this portfolio. Not affiliated with or endorsed by PlanetScale.",
 "ja": "このポートフォリオのための自主制作です。PlanetScale社とは関係ありません。",
 "fr": "Projet personnel réalisé pour ce portfolio. Sans lien avec PlanetScale."},

# 02 — 伊豆（AI で切る実験）
"w2_kicker": {"en": "02 · Live action · an experiment in AI-first editing", "ja": "02 · 実写 · AIに切らせる実験", "fr": "02 · Prises de vue réelles · une expérience de montage par l’IA"},
"w2_title": {"en": "Mt. Daruma, Izu", "ja": "伊豆・達磨山", "fr": "Mont Daruma, Izu"},
"w2_format": {"en": "65 s, 16:9, English subtitles from French", "ja": "65秒・横・フランス語の会話に英語字幕", "fr": "65 s en 16:9, sous-titres anglais à partir du français"},
"w2_source": {"en": "35 min of handheld footage from one day, shot scenery-heavy on purpose", "ja": "1日分の手持ち映像35分。あえて景色を多めに撮影", "fr": "35 min de rushes tournés en un jour, volontairement riches en paysages"},
"w2_role": {
 "en": "Filmed with my wife. Cut by AI, with one fix by hand",
 "ja": "撮影は妻と2人。カットはAI、手で直したのは1か所だけ",
 "fr": "Filmé avec ma femme. Monté par l’IA, une seule correction à la main"},
"w2_h": {"en": "What the test shows", "ja": "この実験でわかったこと", "fr": "Ce que montre l’expérience"},
"w2_b1": {
 "en": "I shot this trip with a lot of silent scenery on purpose, to see how an AI-first edit handles footage with no one talking.",
 "ja": "誰も喋っていない景色を、あえて多めに撮りました。話し声のない素材を、AIがどう切るかを見るためです。",
 "fr": "J’ai volontairement filmé beaucoup de paysages silencieux, pour voir comment un montage fait par l’IA traite des images où personne ne parle."},
"w2_b2": {
 "en": "Where there is speech, the AI cuts well: the monologue is trimmed to the word, carried over the climb with L-cuts.",
 "ja": "声がある所は、AIはうまく切ります。独白は1語単位で整えられ、登りの映像の上にL字カットで流れていきます。",
 "fr": "Là où l’on parle, l’IA coupe bien : le monologue est taillé au mot près et porté sur la montée par des coupes en L."},
"w2_b3": {
 "en": "Silent shots come out too short. The Mt. Fuji reveal gets 1.4 seconds. At the end, it kept the start and finish of a 360° spin and dropped the middle, so the view stood still on both sides of the cut.",
 "ja": "無音のカットは短すぎます。富士山が見える一番の見せ場が1.4秒。最後は360度ぐるっと回るカットの、始まりと終わりだけを残して真ん中を切ったので、つなぎ目の前後で景色が止まって見えていました。",
 "fr": "Les plans silencieux sont trop courts. L’apparition du mont Fuji dure 1,4 seconde. À la fin, elle avait gardé le début et la fin d’un tour à 360° en coupant le milieu : le paysage semblait figé des deux côtés de la coupe."},
"w2_b4": {
 "en": "My one fix: the spin now plays whole, and the film fades out on it. Everything else is the AI’s cut, left as is, and so is the full 14-minute episode on our channel, where I only lengthened a few views. How long a view breathes is still my call.",
 "ja": "手で直したのはそこだけです。回転は切らずに最後まで見せ、そのままフェードアウト。ほかはAIのカットのままです。チャンネルで公開した14分の本編も同じで、景色を少し伸ばしただけ。景色を何秒見せるかは、今も自分で決めています。",
 "fr": "Ma seule correction : le tour se joue en entier, et le film s’éteint dessus. Tout le reste est le montage de l’IA, laissé tel quel, comme l’épisode complet de 14 minutes sur notre chaîne, où j’ai seulement rallongé quelques plans. Combien de temps laisser respirer un paysage, c’est encore moi qui le décide."},

# 03
"w3_kicker": {"en": "03 · Brand motion · YouTube intro", "ja": "03 · ブランドの動き · YouTubeのイントロ", "fr": "03 · Motion design de marque · générique YouTube"},
"w3_title": {"en": "Maison Uchi", "ja": "Maison Uchi", "fr": "Maison Uchi"},
"w3_format": {
 "en": "11 s intro + a 12 s version that dissolves into the first shot (ProRes 4444 with alpha)",
 "ja": "11秒のイントロ＋最初のカットに溶ける12秒版（背景透過のProRes 4444）",
 "fr": "Générique de 11 s + version de 12 s qui se fond dans le premier plan (ProRes 4444 avec alpha)"},
"w3_role": {"en": "Art direction, animation, score", "ja": "デザインの方向付け・動き・音楽", "fr": "Direction artistique, animation, musique"},
"w3_b1": {
 "en": "Drawn in the channel’s own art direction: shin-hanga prints meet 1930s French travel posters.",
 "ja": "チャンネルのデザインの方向性（新版画×1930年代フランスの旅行ポスター）の中で描いています。",
 "fr": "Dessiné dans la direction artistique de la chaîne : l’estampe shin-hanga rencontre l’affiche de voyage française des années 1930."},
"w3_b2": {
 "en": "Introduces the three of us on the beat, then lands the title on the final chord.",
 "ja": "拍に合わせて3人を紹介し、最後の和音でタイトルが決まる。",
 "fr": "Présente nous trois en rythme, puis pose le titre sur le dernier accord."},
"w3_b3": {
 "en": "The music is composed to the exact length, so nothing is cut off at the end.",
 "ja": "音楽は映像の長さぴったりに作っているので、最後に途中で切れない。",
 "fr": "La musique est composée à la durée exacte : rien n’est coupé à la fin."},

# 04
"w4_kicker": {"en": "04 · Short-form · Instagram", "ja": "04 · ショート動画 · Instagram", "fr": "04 · Formats courts · Instagram"},
"w4_title": {"en": "Shot and edited every night", "ja": "毎晩、撮って編集して投稿", "fr": "Tourné et monté chaque soir"},
"w4_link": {"en": "Watch the reel ↗", "ja": "リールを見る ↗", "fr": "Voir le reel ↗"},
"st_views": {"en": "views", "ja": "再生", "fr": "vues"},
"st_skip": {"en": "skip rate", "ja": "スキップ率", "fr": "taux de skip"},
"st_saves": {"en": "saves", "ja": "保存", "fr": "enregistrements"},
"w4_p": {
 "en": "Short videos of daily life as a French–Japanese couple, filmed and edited by me, with my wife on camera. The skip rate is the number I watch: it says whether the first second earns the rest.",
 "ja": "日仏夫婦の日常のショート動画。撮影と編集は自分、出演は妻です。いちばん見ている数字はスキップ率。最初の1秒が、残りを見てもらえるかを決めるからです。",
 "fr": "Des vidéos courtes sur notre quotidien de couple franco-japonais, filmées et montées par moi, avec ma femme à l’écran. Le chiffre que je surveille, c’est le taux de skip : il dit si la première seconde donne envie de voir la suite."},

# process
"pr_kicker": {"en": "How I work", "ja": "進め方", "fr": "Ma méthode"},
"pr_title": {"en": "AI does the repetition. I make the calls.", "ja": "繰り返しはAIに。判断は自分で。", "fr": "L’IA fait la répétition. Je fais les choix."},
"p1h": {"en": "Story first", "ja": "まず話の芯", "fr": "L’histoire d’abord"},
"p1": {"en": "Find the one line or image the piece is about, and cut toward it.", "ja": "その作品が何の話かを1行か1枚の画で見つけ、そこに向かって切る。", "fr": "Trouver la phrase ou l’image qui porte le film, et monter vers elle."},
"p2h": {"en": "Rough cut fast", "ja": "粗編集は速く", "fr": "Prémontage rapide"},
"p2": {"en": "Transcribe everything, pull selects and timings by script, assemble in minutes.", "ja": "全部を書き起こし、台本から素材と時刻を拾って、数分で組む。", "fr": "Tout retranscrire, choisir les plans et les timings depuis le script, assembler en quelques minutes."},
"p3h": {"en": "Taste pass", "ja": "感覚の仕上げ", "fr": "La touche finale"},
"p3": {"en": "How long a silent shot breathes, what to cut, the rhythm between lines. AI cuts well on speech; this part is still mine.", "ja": "無音のカットを何秒見せるか、何を捨てるか、言葉の間。声で切るのはAIが得意。ここはまだ自分の仕事。", "fr": "Combien de temps laisser respirer un plan muet, quoi couper, le rythme entre les répliques. L’IA coupe bien sur la parole ; cette partie reste la mienne."},
"p4h": {"en": "Check by machine", "ja": "機械で検品", "fr": "Contrôle automatique"},
"p4": {"en": "Contact sheets of key frames, loudness, and speech checks before anything ships.", "ja": "要所の静止画、音量、聞き取りを、出す前に機械で確かめる。", "fr": "Planches d’images clés, niveau sonore et intelligibilité vérifiés avant toute livraison."},

# about
"ab_kicker": {"en": "About", "ja": "経歴", "fr": "Parcours"},
"ab_name": {"en": "Kentaro Maeda", "ja": "前田健太郎", "fr": "Kentaro Maeda"},
"ab1": {
 "en": "I’m a video editor in Kamakura, Japan. I spent five years producing client videos from concept to delivery: events, restaurants, outdoor gear, artists and business owners. One of them passed a million views.",
 "ja": "鎌倉に住む映像編集者です。企業のPR映像を企画から納品まで5年間つくってきました。イベント、飲食店、アウトドア用品、アーティストや経営者の紹介映像など。そのうち1本はSNSで100万再生を超えました。",
 "fr": "Je suis monteur vidéo à Kamakura. Pendant cinq ans, j’ai produit des vidéos pour des clients, de l’idée à la livraison : événements, restaurants, matériel de plein air, portraits d’artistes et de chefs d’entreprise. L’une d’elles a dépassé le million de vues."},
"ab2": {
 "en": "I’ve been a dancer and performer for twenty years, on stages from festivals in Japan to the streets of Cambodia. That is where my sense of timing comes from. I also host a show on FM Shonan, a local radio station, which taught me what keeps a conversation moving.",
 "ja": "ダンサーとして20年、国内のフェスからカンボジアの路上まで踊ってきました。編集の「間」の感覚はここから来ています。FM湘南でラジオ番組も担当していて、会話を止めない間の取り方はそこで身につけました。",
 "fr": "Je danse et je suis sur scène depuis vingt ans, des festivals japonais aux rues du Cambodge. C’est de là que vient mon sens du rythme. J’anime aussi une émission sur FM Shonan, une radio locale, qui m’a appris ce qui fait avancer une conversation."},
"ab3": {
 "en": "Today I run a YouTube channel with my wife in French and Japanese, and I build my own tools with Claude, Remotion and Python.",
 "ja": "今は妻とフランス語・日本語のYouTubeチャンネルを運営しながら、Claude・Remotion・Pythonで自分の道具をつくっています。",
 "fr": "Aujourd’hui, je tiens avec ma femme une chaîne YouTube en français et en japonais, et je fabrique mes propres outils avec Claude, Remotion et Python."},
"x1": {"en": "Freelance video producer &amp; editor", "ja": "フリーランス映像制作・編集", "fr": "Réalisateur-monteur indépendant"},
"x2": {"en": "Radio host, FM Shonan", "ja": "ラジオパーソナリティ（FM湘南）", "fr": "Animateur radio, FM Shonan"},
"x3": {"en": "Photographer &amp; videographer, nursery school", "ja": "保育園の撮影担当", "fr": "Photographe et vidéaste, crèche"},
"x4": {"en": "Dancer &amp; performer · Special Award, Moonwalk World Championship", "ja": "ダンサー · ムーンウォーク世界大会 特別賞", "fr": "Danseur · prix spécial, championnat du monde de moonwalk"},
"x5": {"en": "Maison Uchi, YouTube (FR/JP), co-creator &amp; editor", "ja": "Maison Uchi（YouTube・仏日）共同制作・編集", "fr": "Maison Uchi, YouTube (FR/JP), co-créateur et monteur"},
"x6": {"en": "Kurume University, Dept. of Information Society", "ja": "久留米大学 情報社会学科", "fr": "Université de Kurume, département Société de l’information"},
"present": {"en": "present", "ja": "現在", "fr": "en cours"},
"resume": {"en": "Resume (PDF)", "ja": "英文レジュメ（PDF）", "fr": "CV en anglais (PDF)"},

"ft_h": {"en": "Let’s make something people watch to the end.", "ja": "最後まで見てもらえるものを、一緒に。", "fr": "Faisons des vidéos qu’on regarde jusqu’au bout."},
"ft_fine": {
 "en": "© 2026 Kentaro Maeda. Work 01 is a spec piece, not affiliated with PlanetScale.",
 "ja": "© 2026 前田健太郎。作品01は自主制作で、PlanetScale社とは関係ありません。",
 "fr": "© 2026 Kentaro Maeda. Le projet 01 est personnel et sans lien avec PlanetScale."},
}
