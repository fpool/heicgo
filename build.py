# -*- coding: utf-8 -*-
"""HeicGo 多语言页面生成器
运行: python build.py  → 生成 index.html(en) + de/fr/es/ja/zh.html
加语言: 在 LANGS 里加一个条目,重跑即可
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# ---------------- 翻译字典 ----------------
T = {
"en": {
 "name":"English","file":"index.html","title_suffix":"HeicGo",
 "meta":"Convert iPhone HEIC/HEIF photos to JPG online for free. 100% private — files never leave your browser. Batch conversion, no signup, no watermark.",
 "h1":"HEIC to JPG Converter",
 "sub":'Convert iPhone HEIC/HEIF photos to JPG — <b>free</b>, <b>batch</b>, and <b>100% private</b>. Files never leave your browser.',
 "drop_main":"<b>Drop HEIC photos here</b> or click to choose files",
 "drop_hint":".heic / .heif — batch supported · also accepts JPG / PNG / WebP to re-encode",
 "quality":"JPG quality:",
 "privacy":'🔒 <b>Privacy by design:</b> this tool runs entirely in your browser using WebAssembly. Your photos are <b>never uploaded</b> to any server — works offline once loaded.',
 "why_h2":"Why convert HEIC to JPG?",
 "why_p":"iPhone saves photos as HEIC (High Efficiency Image Container) to save storage, but Windows, older software and many websites still can't open it. JPG is the universal format that works everywhere — email, WeChat, online forms, printers and every photo editor.",
 "f1_t":"⚡ Instant batch conversion","f1_d":"Convert dozens of photos at once, download everything as a single ZIP.",
 "f2_t":"🔒 Nothing gets uploaded","f2_d":"Conversion happens on your device. Safe for private photos.",
 "f3_t":"🆓 Free forever","f3_d":"No signup, no watermark, no daily limits, no hidden fees.",
 "how_h2":"How it works",
 "how":['Drop your HEIC files into the box above.','Pick a JPG quality (92% is recommended — visually identical to the original).','Download converted files one by one, or grab them all as a ZIP.'],
 "faq_h2":"FAQ",
 "faq":[("Is it really private?","Yes. Unlike most online converters, there is no upload step — the decoder runs as WebAssembly inside your browser, so your photos never touch a server."),
        ("Does it work on iPhone and Android?","Yes. It works in any modern mobile or desktop browser."),
        ("What about HEIC images with multiple photos?","iPhone \"burst\" or depth-effect files may contain several images — we convert all of them automatically."),
        ("Why did my file convert with lower quality?","JPG is a lossy format. Choose \"Best (92%)\" or \"Max (100%)\" for near-original quality.")],
 "footer":"HeicGo — free private image tools. © 2026",
 "s1":"Converting","s2":"converted","s3":"failed (unsupported file?)","s4":"Packing ZIP...","s5":"ZIP ready",
 "drop_txt":"📸","drop_b":"Drop HEIC photos here",
 "q1":"High (80%)","q2":"Best (92%)","q3":"Max (100%)","dl":"Download JPG","zip":"⬇ Download all as ZIP",
},
"de": {
 "name":"Deutsch","file":"de.html","title_suffix":"HeicGo",
 "meta":"Konvertiere iPhone HEIC/HEIF-Fotos kostenlos online zu JPG. 100 % privat — Dateien verlassen niemals deinen Browser. Stapelkonvertierung, keine Anmeldung, kein Wasserzeichen.",
 "h1":"HEIC zu JPG Konverter",
 "sub":'Konvertiere iPhone HEIC/HEIF-Fotos zu JPG — <b>kostenlos</b>, <b>Stapelverarbeitung</b> und <b>100 % privat</b>. Deine Dateien verlassen den Browser nie.',
 "drop_main":"<b>HEIC-Fotos hier ablegen</b> oder klicken, um Dateien auszuwählen",
 "drop_hint":".heic / .heif — Stapelverarbeitung · auch JPG / PNG / WebP möglich",
 "quality":"JPG-Qualität:",
 "privacy":'🔒 <b>Privatsphäre von Anfang an:</b> Dieses Tool läuft vollständig in deinem Browser per WebAssembly. Deine Fotos werden <b>nie hochgeladen</b> — funktioniert sogar offline.',
 "why_h2":"Warum HEIC in JPG umwandeln?",
 "why_p":"Das iPhone speichert Fotos als HEIC (High Efficiency Image Container), um Speicher zu sparen — aber Windows, ältere Programme und viele Webseiten können das Format nicht öffnen. JPG ist das universelle Format, das überall funktioniert: E-Mail, Online-Formulare, Drucker und jeder Bildeditor.",
 "f1_t":"⚡ Sofortige Stapelkonvertierung","f1_d":"Dutzende Fotos auf einmal umwandeln und alles als ZIP herunterladen.",
 "f2_t":"🔒 Nichts wird hochgeladen","f2_d":"Die Konvertierung erfolgt auf deinem Gerät. Sicher auch für private Fotos.",
 "f3_t":"🆓 Für immer kostenlos","f3_d":"Keine Anmeldung, kein Wasserzeichen, keine Limits, keine versteckten Kosten.",
 "how_h2":"So funktioniert es",
 "how":['Ziehe deine HEIC-Dateien in das Feld oben.','Wähle die JPG-Qualität (92 % empfohlen — optisch identisch zum Original).','Lade die Dateien einzeln oder alle zusammen als ZIP herunter.'],
 "faq_h2":"Häufige Fragen",
 "faq":[("Ist es wirklich privat?","Ja. Anders als bei den meisten Online-Konvertern gibt es keinen Upload — der Decoder läuft als WebAssembly in deinem Browser. Deine Fotos erreichen nie einen Server."),
        ("Funktioniert es auf iPhone und Android?","Ja, in jedem modernen Browser — mobil und am Desktop."),
        ("Was ist mit HEIC-Dateien mit mehreren Bildern?","iPhone-Burst- oder Tiefenfotos können mehrere Bilder enthalten — wir wandeln alle automatisch um."),
        ("Warum ist meine Datei schlechter geworden?","JPG ist ein verlustbehaftetes Format. Wähle „Best (92 %)“ oder „Max (100 %)“ für nahezu Originalqualität.")],
 "footer":"HeicGo — kostenlose private Bild-Tools. © 2026",
 "s1":"Konvertiere","s2":"konvertiert","s3":"fehlgeschlagen (Datei nicht unterstützt?)","s4":"ZIP wird erstellt...","s5":"ZIP bereit",
 "drop_txt":"📸","drop_b":"HEIC-Fotos hier ablegen",
 "q1":"Hoch (80%)","q2":"Beste (92%)","q3":"Maximal (100%)","dl":"JPG herunterladen","zip":"⬇ Alle als ZIP herunterladen",
},
"fr": {
 "name":"Français","file":"fr.html","title_suffix":"HeicGo",
 "meta":"Convertissez gratuitement vos photos iPhone HEIC/HEIF en JPG en ligne. 100 % privé — les fichiers ne quittent jamais votre navigateur. Conversion par lot, sans inscription ni filigrane.",
 "h1":"Convertisseur HEIC en JPG",
 "sub":'Convertissez vos photos iPhone HEIC/HEIF en JPG — <b>gratuit</b>, <b>par lot</b> et <b>100 % privé</b>. Les fichiers ne quittent jamais votre navigateur.',
 "drop_main":"<b>Déposez vos photos HEIC ici</b> ou cliquez pour choisir des fichiers",
 "drop_hint":".heic / .heif — conversion par lot · accepte aussi JPG / PNG / WebP",
 "quality":"Qualité JPG :",
 "privacy":'🔒 <b>Confidentialité par conception :</b> cet outil fonctionne entièrement dans votre navigateur via WebAssembly. Vos photos ne sont <b>jamais téléversées</b> — fonctionne même hors ligne.',
 "why_h2":"Pourquoi convertir HEIC en JPG ?",
 "why_p":"L'iPhone enregistre les photos en HEIC (High Efficiency Image Container) pour économiser de l'espace, mais Windows, les anciens logiciels et de nombreux sites ne peuvent pas ouvrir ce format. Le JPG est le format universel qui fonctionne partout : e-mail, formulaires en ligne, imprimantes et tous les éditeurs photo.",
 "f1_t":"⚡ Conversion par lot instantanée","f1_d":"Convertissez des dizaines de photos d'un coup et téléchargez tout en un seul ZIP.",
 "f2_t":"🔒 Rien n'est téléversé","f2_d":"La conversion se fait sur votre appareil. Sûr même pour les photos privées.",
 "f3_t":"🆓 Gratuit pour toujours","f3_d":"Sans inscription, sans filigrane, sans limite quotidienne, sans frais cachés.",
 "how_h2":"Comment ça marche",
 "how":['Déposez vos fichiers HEIC dans la zone ci-dessus.','Choisissez la qualité JPG (92 % recommandé — visuellement identique à l\'original).','Téléchargez les fichiers un par un, ou tout en un ZIP.'],
 "faq_h2":"FAQ",
 "faq":[("Est-ce vraiment privé ?","Oui. Contrairement à la plupart des convertisseurs en ligne, il n'y a aucun téléversement — le décodeur fonctionne en WebAssembly dans votre navigateur. Vos photos ne touchent jamais un serveur."),
        ("Cela fonctionne-t-il sur iPhone et Android ?","Oui, dans tout navigateur moderne, sur mobile et ordinateur."),
        ("Et les fichiers HEIC contenant plusieurs photos ?","Les fichiers rafale ou à effet de profondeur de l'iPhone peuvent contenir plusieurs images — nous les convertissons toutes automatiquement."),
        ("Pourquoi la qualité est-elle inférieure ?","Le JPG est un format avec perte. Choisissez « Best (92 %) » ou « Max (100 %) » pour une qualité quasi identique.")],
 "footer":"HeicGo — outils d'images gratuits et privés. © 2026",
 "s1":"Conversion","s2":"converti(s)","s3":"échec (fichier non pris en charge ?)","s4":"Création du ZIP...","s5":"ZIP prêt",
 "drop_txt":"📸","drop_b":"Déposez vos photos HEIC ici",
 "q1":"Élevée (80%)","q2":"Meilleure (92%)","q3":"Maximale (100%)","dl":"Télécharger le JPG","zip":"⬇ Tout télécharger en ZIP",
},
"es": {
 "name":"Español","file":"es.html","title_suffix":"HeicGo",
 "meta":"Convierte fotos HEIC/HEIF de iPhone a JPG online gratis. 100 % privado — los archivos nunca salen de tu navegador. Conversión por lotes, sin registro ni marca de agua.",
 "h1":"Convertidor de HEIC a JPG",
 "sub":'Convierte fotos HEIC/HEIF de iPhone a JPG — <b>gratis</b>, <b>por lotes</b> y <b>100 % privado</b>. Los archivos nunca salen de tu navegador.',
 "drop_main":"<b>Arrastra tus fotos HEIC aquí</b> o haz clic para elegir archivos",
 "drop_hint":".heic / .heif — lotes admitidos · también JPG / PNG / WebP",
 "quality":"Calidad JPG:",
 "privacy":'🔒 <b>Privacidad por diseño:</b> esta herramienta funciona por completo en tu navegador con WebAssembly. Tus fotos <b>nunca se suben</b> a ningún servidor — funciona incluso sin conexión.',
 "why_h2":"¿Por qué convertir HEIC a JPG?",
 "why_p":"El iPhone guarda las fotos en HEIC (High Efficiency Image Container) para ahorrar espacio, pero Windows, programas antiguos y muchos sitios web no pueden abrirlo. JPG es el formato universal que funciona en todas partes: correo electrónico, formularios en línea, impresoras y cualquier editor de fotos.",
 "f1_t":"⚡ Conversión por lotes al instante","f1_d":"Convierte decenas de fotos a la vez y descárgalas todo en un solo ZIP.",
 "f2_t":"🔒 Nada se sube","f2_d":"La conversión ocurre en tu dispositivo. Seguro incluso para fotos privadas.",
 "f3_t":"🆓 Gratis para siempre","f3_d":"Sin registro, sin marca de agua, sin límites diarios, sin costes ocultos.",
 "how_h2":"Cómo funciona",
 "how":['Arrastra tus archivos HEIC al recuadro de arriba.','Elige la calidad JPG (92 % recomendado — visualmente idéntico al original).','Descarga los archivos uno a uno o todos juntos en un ZIP.'],
 "faq_h2":"Preguntas frecuentes",
 "faq":[("¿De verdad es privado?","Sí. A diferencia de la mayoría de convertidores online, no hay subida — el decodificador funciona como WebAssembly dentro de tu navegador. Tus fotos nunca llegan a un servidor."),
        ("¿Funciona en iPhone y Android?","Sí, en cualquier navegador moderno, móvil o de escritorio."),
        ("¿Y los archivos HEIC con varias fotos?","Los archivos de ráfaga o con efecto de profundidad del iPhone pueden contener varias imágenes — las convertimos todas automáticamente."),
        ("¿Por qué salió con menos calidad?","JPG es un formato con pérdida. Elige «Best (92 %)» o «Max (100 %)» para una calidad casi idéntica.")],
 "footer":"HeicGo — herramientas de imagen gratuitas y privadas. © 2026",
 "s1":"Convirtiendo","s2":"convertido(s)","s3":"fallido (¿archivo no compatible?)","s4":"Empaquetando ZIP...","s5":"ZIP listo",
 "drop_txt":"📸","drop_b":"Arrastra tus fotos HEIC aquí",
 "q1":"Alta (80%)","q2":"Mejor (92%)","q3":"Máxima (100%)","dl":"Descargar JPG","zip":"⬇ Descargar todo en ZIP",
},
"ja": {
 "name":"日本語","file":"ja.html","title_suffix":"HeicGo",
 "meta":"iPhoneのHEIC/HEIF写真を無料でオンラインJPG変換。100%プライベート — ファイルはブラウザから出ません。一括変換、登録不要、透かしなし。",
 "h1":"HEIC → JPG 変換ツール",
 "sub":'iPhoneのHEIC/HEIF写真をJPGに変換 — <b>無料</b>・<b>一括処理</b>・<b>100%プライベート</b>。ファイルはブラウザの外に出ません。',
 "drop_main":"<b>ここにHEIC写真をドロップ</b>、またはクリックしてファイルを選択",
 "drop_hint":".heic / .heif — 一括対応 · JPG / PNG / WebP も再エンコード可能",
 "quality":"JPG 品質:",
 "privacy":'🔒 <b>プライバシー・バイ・デザイン:</b> このツールは WebAssembly により完全にブラウザ内で動作します。写真がサーバーに<b>アップロードされることは一切ありません</b> — オフラインでも動作します。',
 "why_h2":"なぜ HEIC を JPG に変換するのか",
 "why_p":"iPhoneは容量を節約するため写真をHEIC(High Efficiency Image Container)形式で保存しますが、Windowsや古いソフト、多くのウェブサイトでは開けません。JPGはメール、Webフォーム、プリンター、あらゆる画像エディタで使えるユニバーサル形式です。",
 "f1_t":"⚡ 一括変換","f1_d":"数十枚の写真を一度に変換し、ZIPでまとめてダウンロード。",
 "f2_t":"🔒 アップロード一切なし","f2_d":"変換はあなたのデバイス上で実行。プライベートな写真も安全です。",
 "f3_t":"🆓 永久無料","f3_d":"登録不要、透かしなし、日制限なし、隠れた費用もなし。",
 "how_h2":"使い方",
 "how":['上のボックスにHEICファイルをドロップします。','JPG品質を選択(92%推奨 — 見た目はオリジナルと同一)。','変換後のファイルを1枚ずつ、またはZIPで一括ダウンロード。'],
 "faq_h2":"よくある質問",
 "faq":[("本当にプライベートですか?","はい。ほとんどのオンライン変換ツールと違い、アップロード処理がありません — デコーダはブラウザ内のWebAssemblyで動くため、写真がサーバーに送信されることはありません。"),
        ("iPhoneやAndroidで使えますか?","はい。モバイル/デスクトップの最新ブラウザで動作します。"),
        ("複数画像を含むHEICファイルは?","iPhoneのバーストや被写界深度効果のファイルには複数画像が含まれることがあります — すべて自動で変換します。"),
        ("画質が落ちたのはなぜ?","JPGは非可逆圧縮です。「Best (92%)」または「Max (100%)」を選ぶとほぼオリジナル同等の品質になります。")],
 "footer":"HeicGo — 無料・プライベートな画像ツール. © 2026",
 "s1":"変換中","s2":"件変換完了","s3":"件失敗(未対応ファイル?)","s4":"ZIP作成中...","s5":"ZIP完成",
 "drop_txt":"📸","drop_b":"ここにHEIC写真をドロップ",
 "q1":"高 (80%)","q2":"最高 (92%)","q3":"最大 (100%)","dl":"JPGをダウンロード","zip":"⬇ すべてZIPでダウンロード",
},
"ko": {
 "name":"한국어","file":"ko.html","title_suffix":"HeicGo",
 "meta":"iPhone HEIC/HEIF 사진을 무료로 온라인에서 JPG로 변환하세요. 100% 비공개 — 파일은 브라우저를 벗어나지 않습니다. 일괄 변환, 가입 불필요, 워터마크 없음.",
 "h1":"HEIC → JPG 변환 도구",
 "sub":'iPhone HEIC/HEIF 사진을 JPG로 변환 — <b>무료</b>, <b>일괄 처리</b>, <b>100% 비공개</b>. 파일은 브라우저 밖으로 나가지 않습니다.',
 "drop_main":"<b>여기에 HEIC 사진을 끌어다 놓기</b> 또는 클릭해서 파일 선택",
 "drop_hint":".heic / .heif — 일괄 처리 지원 · JPG / PNG / WebP도 재인코딩 가능",
 "quality":"JPG 품질:",
 "privacy":'🔒 <b>설계된 프라이버시:</b> 이 도구는 WebAssembly로 브라우저 안에서 완전히 실행됩니다. 사진은 서버에 <b>업로드되지 않습니다</b> — 로드 후 오프라인에서도 작동합니다.',
 "why_h2":"왜 HEIC를 JPG로 변환해야 할까요?",
 "why_p":"iPhone은 저장 공간을 아끼기 위해 사진을 HEIC(High Efficiency Image Container) 형식으로 저장하지만, Windows와 구형 소프트웨어, 많은 웹사이트에서 열 수 없습니다. JPG는 이메일, 웹 양식, 프린터, 모든 사진 편집기에서 작동하는 범용 형식입니다.",
 "f1_t":"⚡ 즉시 일괄 변환","f1_d":"수십 장의 사진을 한 번에 변환하고 ZIP 하나로 모두 다운로드하세요.",
 "f2_t":"🔒 업로드 없음","f2_d":"변환은 기기에서 이루어집니다. 개인 사진도 안전합니다.",
 "f3_t":"🆓 영구 무료","f3_d":"가입 없음, 워터마크 없음, 일일 제한 없음, 숨은 비용 없음.",
 "how_h2":"사용 방법",
 "how":['위의 박스에 HEIC 파일을 끌어다 놓으세요.','JPG 품질을 선택하세요(92% 권장 — 원본과 육안으로 동일).','변환된 파일을 하나씩 다운로드하거나 ZIP으로 한 번에 받으세요.'],
 "faq_h2":"자주 묻는 질문",
 "faq":[("정말 비공개인가요?","네. 대부분의 온라인 변환기와 달리 업로드 단계가 없습니다 — 디코더는 브라우저 안의 WebAssembly로 실행되므로 사진이 서버에 전송되지 않습니다."),
        ("iPhone과 Android에서 작동하나요?","네. 모바일 및 데스크톱의 최신 브라우저에서 작동합니다."),
        ("여러 장의 사진이 담긴 HEIC 파일은?","iPhone의 버스트나 인물 모드 파일에는 여러 이미지가 포함될 수 있습니다 — 모두 자동으로 변환합니다."),
        ("품질이 낮아진 이유는?","JPG는 손실 압축 형식입니다. \"Best (92%)\" 또는 \"Max (100%)\"를 선택하면 원본에 가까운 품질이 유지됩니다.")],
 "footer":"HeicGo — 무료 사설 이미지 도구. © 2026",
 "s1":"변환 중","s2":"개 변환 완료","s3":"개 실패(지원되지 않는 파일?)","s4":"ZIP 압축 중...","s5":"ZIP 준비 완료",
 "drop_txt":"📸","drop_b":"여기에 HEIC 사진을 끌어다 놓기",
 "q1":"높음 (80%)","q2":"최상 (92%)","q3":"최대 (100%)","dl":"JPG 다운로드","zip":"⬇ 모두 ZIP으로 다운로드",
},
"zh-cn": {
 "name":"简体中文","file":"zh-cn.html","title_suffix":"HeicGo",
 "meta":"免费在线把 iPhone HEIC/HEIF 照片转换成 JPG。100% 隐私安全——文件永不离开浏览器。支持批量、免注册、无水印。",
 "h1":"HEIC 转 JPG 工具",
 "sub":'把 iPhone 的 HEIC/HEIF 照片转成 JPG — <b>免费</b>、<b>支持批量</b>、<b>100% 隐私安全</b>。文件永不离开你的浏览器。',
 "drop_main":"<b>把 HEIC 照片拖到这里</b>，或点击选择文件",
 "drop_hint":".heic / .heif — 支持批量 · 也接受 JPG / PNG / WebP 重新编码",
 "quality":"JPG 质量：",
 "privacy":'🔒 <b>隐私是设计出来的：</b>本工具通过 WebAssembly 完全在你的浏览器内运行。照片<b>永不上传</b>到任何服务器——加载后离线也能用。',
 "why_h2":"为什么要把 HEIC 转成 JPG？",
 "why_p":"iPhone 为节省存储空间，默认用 HEIC（高效率图像容器）保存照片，但 Windows、老软件和很多网站都打不开它。JPG 是通行天下的通用格式——邮件、网页表单、打印机、所有修图软件都认。",
 "f1_t":"⚡ 批量秒转","f1_d":"一次几十张，打包一个 ZIP 全部下载。",
 "f2_t":"🔒 零上传","f2_d":"转换发生在你自己的设备上，私密照片也放心。",
 "f3_t":"🆓 永久免费","f3_d":"免注册、无水印、无次数限制、没有隐藏收费。",
 "how_h2":"使用方法",
 "how":['把 HEIC 文件拖进上面的方框。','选择 JPG 质量（推荐 92%——肉眼与原图无异）。','逐张下载，或打包 ZIP 一次拿走。'],
 "faq_h2":"常见问题",
 "faq":[("真的不会上传我的照片吗？","真的。和大多数在线转换器不同，这里没有上传环节——解码器以 WebAssembly 形式在浏览器内运行，照片根本不会经过任何服务器。"),
        ("手机上能用吗？","能。任何现代浏览器（手机/电脑）都可以。"),
        ("一个 HEIC 里有多张照片怎么办？","iPhone 的连拍、景深照片可能包含多张图——我们会全部自动转出来。"),
        ("为什么画质变差了？","JPG 是有损压缩。选「Best (92%)」或「Max (100%)」即可获得几乎无损的画质。")],
 "footer":"HeicGo — 免费且注重隐私的图片工具。© 2026",
 "s1":"正在转换","s2":"张完成","s3":"张失败（文件不支持？）","s4":"正在打包 ZIP...","s5":"ZIP 已就绪",
 "drop_txt":"📸","drop_b":"把 HEIC 照片拖到这里",
 "q1":"高 (80%)","q2":"最佳 (92%)","q3":"最大 (100%)","dl":"下载 JPG","zip":"⬇ 全部打包下载",
},
"zh-tw": {
 "name":"繁體中文","file":"zh-tw.html","title_suffix":"HeicGo",
 "meta":"免費線上將 iPhone HEIC/HEIF 照片轉換為 JPG。100% 隱私安全——檔案永不離開瀏覽器。支援批次轉換、免註冊、無浮水印。",
 "h1":"HEIC 轉 JPG 工具",
 "sub":'把 iPhone 的 HEIC/HEIF 照片轉成 JPG — <b>免費</b>、<b>支援批次</b>、<b>100% 隱私安全</b>。檔案永不離開你的瀏覽器。',
 "drop_main":"<b>把 HEIC 照片拖到這裡</b>，或點擊選擇檔案",
 "drop_hint":".heic / .heif — 支援批次 · 也接受 JPG / PNG / WebP 重新編碼",
 "quality":"JPG 品質：",
 "privacy":'🔒 <b>隱私是設計出來的：</b>本工具透過 WebAssembly 完全在你的瀏覽器內執行。照片<b>永不上傳</b>到任何伺服器——載入後離線也能用。',
 "why_h2":"為什麼要把 HEIC 轉成 JPG？",
 "why_p":"iPhone 為節省儲存空間，預設用 HEIC（高效率圖像容器）儲存照片，但 Windows、舊軟體和許多網站都打不開它。JPG 是通行天下的通用格式——郵件、網頁表單、印表機、所有修圖軟體都認。",
 "f1_t":"⚡ 批次秒轉","f1_d":"一次幾十張，打包一個 ZIP 全部下載。",
 "f2_t":"🔒 零上傳","f2_d":"轉換發生在你自己的裝置上，私密照片也放心。",
 "f3_t":"🆓 永久免費","f3_d":"免註冊、無浮水印、無次數限制、沒有隱藏收費。",
 "how_h2":"使用方法",
 "how":['把 HEIC 檔案拖進上面的方框。','選擇 JPG 品質（推薦 92%——肉眼與原圖無異）。','逐張下載，或打包 ZIP 一次拿走。'],
 "faq_h2":"常見問題",
 "faq":[("真的不會上傳我的照片嗎？","真的。和大多數線上轉換器不同，這裡沒有上傳環節——解碼器以 WebAssembly 形式在瀏覽器內執行，照片根本不會經過任何伺服器。"),
        ("手機上能用嗎？","能。任何現代瀏覽器（手機/電腦）都可以。"),
        ("一個 HEIC 裡有多張照片怎麼辦？","iPhone 的連拍、景深照片可能包含多張圖——我們會全部自動轉出來。"),
        ("為什麼畫質變差了？","JPG 是破壞性壓縮。選「Best (92%)」或「Max (100%)」即可獲得幾乎無損的畫質。")],
 "footer":"HeicGo — 免費且注重隱私的圖片工具。© 2026",
 "s1":"正在轉換","s2":"張完成","s3":"張失敗（檔案不支援？）","s4":"正在打包 ZIP...","s5":"ZIP 已就緒",
 "drop_txt":"📸","drop_b":"把 HEIC 照片拖到這裡",
 "q1":"高 (80%)","q2":"最佳 (92%)","q3":"最大 (100%)","dl":"下載 JPG","zip":"⬇ 全部打包下載",
},
}

ORDER = ["en","de","fr","es","ja","ko","zh-cn","zh-tw"]

NAV = {
 "en":("Why convert?","How it works","FAQ","Privacy","About"),
 "de":("Warum konvertieren?","Anleitung","FAQ","Datenschutz","Über uns"),
 "fr":("Pourquoi ?","Fonctionnement","FAQ","Confidentialité","À propos"),
 "es":("¿Por qué?","Cómo funciona","Preguntas","Privacidad","Acerca de"),
 "ja":("変換の理由","使い方","よくある質問","プライバシー","サイト情報"),
 "ko":("변환 이유","사용 방법","FAQ","개인정보","소개"),
 "zh-cn":("为什么转换","使用方法","常见问题","隐私政策","关于"),
 "zh-tw":("為什麼轉換","使用方法","常見問題","隱私政策","關於"),
}

BASE = (Path(__file__).parent / "template.html").read_text(encoding="utf-8")
if "PicVault" in BASE:
    raise SystemExit("template.html 里还有 PicVault，请先确认改名完成")

def lang_switcher(cur, href_for=None):
    hf = href_for or (lambda c: T[c]["file"])
    items = "".join(
        f'<a href="{hf(c)}"{" class=\"cur\"" if c==cur else ""}>{T[c]["name"]}</a>'
        for c in ORDER)
    btn = ('<button id="langBtn" aria-haspopup="true" aria-expanded="false">'
           f'{T[cur]["name"]}'
           '<svg class="chev" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>'
           '</button>')
    return f'<div class="lang">{btn}<div class="lang-menu">{items}</div></div>'

def hreflangs(cur):
    lines = [f'  <link rel="alternate" hreflang="{c}" href="https://heicgo-ecc.pages.dev/">' if c == "en"
             else f'  <link rel="alternate" hreflang="{c}" href="https://heicgo-ecc.pages.dev/{c}">' for c in ORDER]
    lines.append('  <link rel="alternate" hreflang="x-default" href="https://heicgo-ecc.pages.dev/">')
    return "\n".join(lines)

def faq_jsonld(t):
    import json as _json
    entities = [{"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]
    return ('<script type="application/ld+json">' +
            _json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                         "mainEntity": entities}, ensure_ascii=False) +
            '</script>')

def build(code):
    t = T[code]
    faq = "".join(f'<p><b>{q}</b> {a}</p>' for q, a in t["faq"])
    how = "".join(f"      <li>{x}</li>\n" for x in t["how"])
    html = BASE
    # head
    html = html.replace(
        '<meta name="description" content="Convert iPhone HEIC/HEIF photos to JPG online for free. 100% private — files never leave your browser. Batch conversion, no signup, no watermark.">',
        f'<meta name="description" content="{t["meta"]}">')
    html = html.replace(
        '<title>HEIC to JPG Converter — Free, Private, No Upload | HeicGo</title>',
        f'<title>{t["h1"]} — Free, Private, No Upload | {t["title_suffix"]}</title>')
    html = html.replace('</title>', '</title>\n' + hreflangs(code), 1)
    canon = "https://heicgo-ecc.pages.dev/" if code == "en" else f"https://heicgo-ecc.pages.dev/{code}"
    html = html.replace('__CANONICAL__', canon)
    html = html.replace('</head>', faq_jsonld(t) + '\n</head>', 1)
    html = html.replace('<html lang="en">', f'<html lang="{code}">')
    # nav 语言下拉 + 导航链接
    nw, nh, nf, npriv, nab = NAV[code]
    html = (html.replace('__NAV_WHY__', nw).replace('__NAV_HOW__', nh).replace('__NAV_FAQ__', nf)
                .replace('__NAV_PRIVACY__', npriv).replace('__NAV_ABOUT__', nab))
    html = html.replace('__LANGSWITCH__', lang_switcher(code))
    # 正文
    html = html.replace("<h1>HEIC to JPG Converter</h1>", f"<h1>{t['h1']}</h1>")
    html = html.replace('class="sub">Convert iPhone HEIC/HEIF photos to JPG — <b>free</b>, <b>batch</b>, and <b>100% private</b>. Files never leave your browser.',
                        f'class="sub">{t["sub"]}')
    html = html.replace('<p><b>Drop HEIC photos here</b> or click to choose files</p>', f'<p>{t["drop_main"]}</p>')
    html = html.replace('class="hint">.heic / .heif — batch supported · also accepts JPG / PNG / WebP to re-encode', f'class="hint">{t["drop_hint"]}')
    html = html.replace('>JPG quality:', f'>{t["quality"]}')
    html = html.replace('<option value="0.8">High (80%)</option><option value="0.92" selected>Best (92%)</option><option value="1">Max (100%)</option>',
        f'<option value="0.8">{t["q1"]}</option><option value="0.92" selected>{t["q2"]}</option><option value="1">{t["q3"]}</option>')
    html = html.replace('class="privacy">🔒 <b>Privacy by design:</b> this tool runs entirely in your browser using WebAssembly. Your photos are <b>never uploaded</b> to any server — works offline once loaded.',
                        f'class="privacy">{t["privacy"]}')
    html = html.replace("<h2>Why convert HEIC to JPG?</h2>", f"<h2>{t['why_h2']}</h2>")
    i = html.find("iPhone saves photos as HEIC")
    html = html[:i] + t["why_p"] + html[html.find("</p>", i) + 4:]
    html = html.replace("<b>⚡ Instant batch conversion</b><span>Convert dozens of photos at once, download everything as a single ZIP.</span>",
                        f"<b>{t['f1_t']}</b><span>{t['f1_d']}</span>")
    html = html.replace("<b>🔒 Nothing gets uploaded</b><span>Conversion happens on your device. Safe for private photos.</span>",
                        f"<b>{t['f2_t']}</b><span>{t['f2_d']}</span>")
    html = html.replace("<b>🆓 Free forever</b><span>No signup, no watermark, no daily limits, no hidden fees.</span>",
                        f"<b>{t['f3_t']}</b><span>{t['f3_d']}</span>")
    html = html.replace("<h2>How it works</h2>", f"<h2>{t['how_h2']}</h2>")
    i = html.find("<ul>")
    html = html[:i] + "<ul>\n" + how + "    </ul>" + html[html.find("</ul>", i) + 5:]
    # FAQ：先在英文锚点处切分注入，再替换标题（顺序不能反，否则 find 失败切坏文档）
    i = html.find('<h2 id="faq">FAQ</h2>')
    j = html.find("</article>")
    if i < 0 or j <= i:
        import sys as _s
        _s.stderr.write(f"[debug] code={code} len={len(html)} faq={i} article={j} "
                        f"faq_word_at={html.find('FAQ')} tail={html[-200:]!r}\n")
    assert i > -1 and j > i, "FAQ 锚点丢失"
    html = html[:i] + f'<h2 id="faq">{t["faq_h2"]}</h2>\n    ' + faq + "\n  " + html[j:]
    html = html.replace('HeicGo — free private image tools. © 2026', t["footer"])
    # JS 文案占位符
    html = (html.replace('__S1__', t["s1"]).replace('__S2__', t["s2"])
                .replace('__S3__', t["s3"]).replace('__S4__', t["s4"])
                .replace('__S5__', t["s5"]).replace('__DL__', t["dl"]))
    html = html.replace('⬇ Download all as ZIP', t["zip"])
    return html

# ---------- 子页面(隐私政策/关于)多语言数据 ----------
CONTACT = "<b>liuyulong667@gmail.com</b>"

PRIV = {
"en": {"title":"Privacy Policy","h1":"Privacy Policy","updated":"October 2, 2026",
 "meta":"HeicGo privacy policy — how we handle data in our browser-based image tools, including cookies and third-party advertising.",
 "intro":"HeicGo (“we”, “our”) operates free browser-based image tools, including the HEIC to JPG converter available at heicgo-ecc.pages.dev. This policy explains what data is — and is not — collected when you use our tools.",
 "sections":[
  ("1. Your photos and files",["<b>We do not collect, store, or transmit your photos.</b> All conversion happens locally in your browser using WebAssembly. When you drop a file into our tools, it is processed by your own device and never uploaded to any server. Closing or reloading the page erases everything."]),
  ("2. Server logs",["Like virtually all websites, our hosting provider (Cloudflare) automatically records standard technical request data — such as IP address, browser type, requested URL, and timestamp — for security and performance purposes. This data is governed by <a href='https://www.cloudflare.com/privacypolicy/'>Cloudflare's privacy policy</a> and is not used to identify individual visitors."]),
  ("3. Cookies and advertising",["We plan to display advertising served by Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this and other sites.","You may opt out of personalized advertising by visiting <a href='https://www.google.com/settings/ads'>Google Ads Settings</a>. You can also control cookies through your browser settings; blocking cookies will not affect the functionality of our tools."]),
  ("4. Local storage",["We use your browser's local storage to remember small preferences such as your theme (light/dark) choice. This data stays on your device and can be removed by clearing your browser storage."]),
  ("5. Children's privacy",["Our tools are general-purpose and do not knowingly collect personal information from children under 13."]),
  ("6. Changes to this policy",["We may update this policy as the service evolves. Material changes will be reflected on this page with an updated date."]),
  ("7. Contact",["Questions about this policy? Reach us at " + CONTACT + "."])]},
"de": {"title":"Datenschutzerklärung","h1":"Datenschutzerklärung","updated":"2. Oktober 2026",
 "meta":"Datenschutzerklärung von HeicGo — wie wir Daten in unseren Browser-Tools behandeln, einschließlich Cookies und Werbung.",
 "intro":"HeicGo („wir“) betreibt kostenlose Browser-Tools für Bilder, darunter den HEIC-zu-JPG-Konverter auf heicgo-ecc.pages.dev. Diese Erklärung beschreibt, welche Daten bei der Nutzung erhoben werden — und welche nicht.",
 "sections":[
  ("1. Ihre Fotos und Dateien",["<b>Wir erfassen, speichern und übertragen Ihre Fotos nicht.</b> Die Konvertierung läuft vollständig lokal in Ihrem Browser per WebAssembly. Dateien werden auf Ihrem Gerät verarbeitet und niemals auf einen Server hochgeladen. Schließen oder Neuladen der Seite löscht alles."]),
  ("2. Serverprotokolle",["Wie praktisch jede Website zeichnet unser Hosting-Anbieter (Cloudflare) automatisch Standard-Anfragedaten auf — IP-Adresse, Browsertyp, URL, Zeitstempel — für Sicherheit und Performance. Diese Daten unterliegen der <a href='https://www.cloudflare.com/privacypolicy/'>Datenschutzerklärung von Cloudflare</a> und dienen nicht zur Identifizierung einzelner Besucher."]),
  ("3. Cookies und Werbung",["Wir planen, Werbung von Google AdSense anzuzeigen. Drittanbieter, einschließlich Google, verwenden Cookies, um auf frühere Besuche basierende Werbung einzublenden.","Personalisierte Werbung können Sie unter <a href='https://www.google.com/settings/ads'>Google Anzeigeneinstellungen</a> deaktivieren. Cookies lassen sich auch über die Browsereinstellungen steuern; ein Blockieren beeinträchtigt die Werkzeuge nicht."]),
  ("4. Lokaler Speicher",["Wir nutzen den lokalen Speicher Ihres Browsers, um kleine Einstellungen wie das Design (hell/dunkel) zu merken. Diese Daten bleiben auf Ihrem Gerät."]),
  ("5. Kinder",["Unsere Werkzeuge sind universell und erfassen wissentlich keine personenbezogenen Daten von Kindern unter 13."]),
  ("6. Änderungen",["Diese Erklärung kann sich mit dem Dienst weiterentwickeln. Wesentliche Änderungen werden auf dieser Seite mit neuem Datum ausgewiesen."]),
  ("7. Kontakt",["Fragen? Schreiben Sie an " + CONTACT + "."])]},
"fr": {"title":"Politique de confidentialité","h1":"Politique de confidentialité","updated":"2 octobre 2026",
 "meta":"Politique de confidentialité de HeicGo — traitement des données dans nos outils d'images navigateur, cookies et publicité tierce.",
 "intro":"HeicGo (« nous ») exploite des outils d'images gratuits fonctionnant dans le navigateur, dont le convertisseur HEIC vers JPG sur heicgo-ecc.pages.dev. Cette politique explique quelles données sont — ou ne sont pas — collectées.",
 "sections":[
  ("1. Vos photos et fichiers",["<b>Nous ne collectons, ne stockons et ne transmettons pas vos photos.</b> La conversion s'effectue localement dans votre navigateur via WebAssembly. Les fichiers sont traités par votre appareil et jamais envoyés à un serveur. Fermer ou recharger la page efface tout."]),
  ("2. Journaux serveur",["Comme presque tous les sites, notre hébergeur (Cloudflare) enregistre automatiquement les données techniques standard — adresse IP, type de navigateur, URL, horodatage — à des fins de sécurité et de performance. Ces données sont régies par la <a href='https://www.cloudflare.com/privacypolicy/'>politique de confidentialité de Cloudflare</a>."]),
  ("3. Cookies et publicité",["Nous prévoyons d'afficher des publicités servies par Google AdSense. Des tiers, dont Google, utilisent des cookies pour diffuser des publicités selon les visites précédentes.","Vous pouvez désactiver la publicité personnalisée via <a href='https://www.google.com/settings/ads'>les paramètres des annonces Google</a> ; bloquer les cookies n'affecte pas nos outils."]),
  ("4. Stockage local",["Nous utilisons le stockage local du navigateur pour mémoriser vos préférences (thème clair/sombre). Ces données restent sur votre appareil."]),
  ("5. Enfants",["Nos outils sont généraux et ne collectent pas sciemment de données personnelles d'enfants de moins de 13 ans."]),
  ("6. Modifications",["Cette politique peut évoluer avec le service ; les changements importants seront indiqués sur cette page avec une date mise à jour."]),
  ("7. Contact",["Des questions ? Écrivez à " + CONTACT + "."])]},
"es": {"title":"Política de privacidad","h1":"Política de privacidad","updated":"2 de octubre de 2026",
 "meta":"Política de privacidad de HeicGo — cómo tratamos los datos en nuestras herramientas de imágenes en el navegador, cookies y publicidad de terceros.",
 "intro":"HeicGo («nosotros») opera herramientas de imágenes gratuitas que funcionan en el navegador, incluido el convertidor de HEIC a JPG disponible en heicgo-ecc.pages.dev. Esta política explica qué datos se recopilan — y cuáles no — al usar nuestras herramientas.",
 "sections":[
  ("1. Tus fotos y archivos",["<b>No recopilamos, almacenamos ni transmitimos tus fotos.</b> La conversión ocurre localmente en tu navegador mediante WebAssembly. Los archivos los procesa tu propio dispositivo y nunca se suben a ningún servidor. Cerrar o recargar la página borra todo."]),
  ("2. Registros del servidor",["Como casi todos los sitios web, nuestro proveedor de alojamiento (Cloudflare) registra automáticamente datos técnicos estándar — dirección IP, tipo de navegador, URL, marca de tiempo — con fines de seguridad y rendimiento. Estos datos se rigen por la <a href='https://www.cloudflare.com/privacypolicy/'>política de privacidad de Cloudflare</a>."]),
  ("3. Cookies y publicidad",["Planeamos mostrar publicidad servida por Google AdSense. Proveedores externos, incluido Google, usan cookies para mostrar anuncios según visitas previsas del usuario.","Puedes desactivar la publicidad personalizada en <a href='https://www.google.com/settings/ads'>Configuración de anuncios de Google</a>; bloquear las cookies no afecta la funcionalidad de nuestras herramientas."]),
  ("4. Almacenamiento local",["Usamos el almacenamiento local del navegador para recordar preferencias como el tema (claro/oscuro). Estos datos permanecen en tu dispositivo."]),
  ("5. Privacidad de menores",["Nuestras herramientas son de uso general y no recopilan a sabiendas información personal de menores de 13 años."]),
  ("6. Cambios en esta política",["Podemos actualizar esta política a medida que evolucione el servicio; los cambios relevantes se reflejarán en esta página con fecha actualizada."]),
  ("7. Contacto",["¿Preguntas? Escríbenos a " + CONTACT + "."])]},
"ja": {"title":"プライバシーポリシー","h1":"プライバシーポリシー","updated":"2026年10月2日",
 "meta":"HeicGoのプライバシーポリシー — ブラウザベースの画像ツールにおけるデータ、Cookie、第三者広告の取り扱い。",
 "intro":"HeicGo(「当社」)は、heicgo-ecc.pages.dev で提供する HEIC→JPG 変換ツールを含む、ブラウザ内で動作する無料の画像ツールを運営しています。本ポリシーは、ツール利用時に収集されるデータ — および収集されないデータ — について説明します。",
 "sections":[
  ("1. 写真とファイルについて",["<b>当社は写真の収集・保存・送信を行いません。</b>変換は WebAssembly によりブラウザ内でローカルに実行されます。ファイルはお客様のデバイスで処理され、サーバーにアップロードされることはありません。ページを閉じたり再読み込みするとすべて消えます。"]),
  ("2. サーバーログ",["ほぼすべてのウェブサイトと同様、ホスティング事業者(Cloudflare)はセキュリティとパフォーマンスのため、IP アドレス、ブラウザ種別、URL、タイムスタンプ等の標準的な技術データを自動記録します。このデータは <a href='https://www.cloudflare.com/privacypolicy/'>Cloudflare のプライバシーポリシー</a>に準拠し、個人を特定するためには使用されません。"]),
  ("3. Cookie と広告",["Google AdSense による広告を表示する予定です。Google を含む第三者ベンダーは、ユーザーの過去のアクセスに基づいて広告を配信するために Cookie を使用します。","パーソナライズ広告は <a href='https://www.google.com/settings/ads'>Google 広告設定</a>で無効化できます。Cookie のブロックはツールの機能に影響しません。"]),
  ("4. ローカルストレージ",["テーマ(ライト/ダーク)などの小さな設定を記憶するためにブラウザのローカルストレージを使用します。このデータは端末上にのみ保存されます。"]),
  ("5. 児童のプライバシー",["当社のツールは汎用であり、13 歳未満の個人情報を意図的に収集することはありません。"]),
  ("6. ポリシーの変更",["サービスの進化に伴い本ポリシーを更新することがあります。重要な変更はこのページに反映されます。"]),
  ("7. お問い合わせ",["ご質問は " + CONTACT + " まで。"])]},
"ko": {"title":"개인정보 처리방침","h1":"개인정보 처리방침","updated":"2026년 10월 2일",
 "meta":"HeicGo 개인정보 처리방침 — 브라우저 기반 이미지 도구, 쿠키 및 제3자 광고의 데이터 처리 방식.",
 "intro":"HeicGo(「당사」)는 heicgo-ecc.pages.dev 에서 제공되는 HEIC→JPG 변환기를 포함해 브라우저에서 실행되는 무료 이미지 도구를 운영합니다. 본 방침은 도구 사용 시 수집되는 데이터 — 그리고 수집되지 않는 데이터 — 를 설명합니다.",
 "sections":[
  ("1. 사진 및 파일",["<b>당사는 사진을 수집·저장·전송하지 않습니다.</b> 변환은 WebAssembly를 통해 브라우저 안에서 로컬로 실행됩니다. 파일은 사용자 기기에서 처리되며 서버로 전송되지 않습니다. 페이지를 닫거나 새로고침하면 모두 지워집니다."]),
  ("2. 서버 로그",["거의 모든 웹사이트와 마찬가지로 호스팅 업체(Cloudflare)는 보안과 성능을 위해 IP 주소, 브라우저 유형, URL, 타임스탬프 등 표준 기술 데이터를 자동 기록합니다. 이 데이터는 <a href='https://www.cloudflare.com/privacypolicy/'>Cloudflare 개인정보 처리방침</a>의 적용을 받으며 개인 식별에 사용되지 않습니다."]),
  ("3. 쿠키와 광고",["Google AdSense 광고를 표시할 계획입니다. Google을 포함한 제3자는 사용자의 이전 방문을 기반으로 광고를 게재하기 위해 쿠키를 사용합니다.","맞춤 광고는 <a href='https://www.google.com/settings/ads'>Google 광고 설정</a>에서 비활성화할 수 있으며, 쿠키를 차단해도 도구 기능에는 영향이 없습니다."]),
  ("4. 로컬 저장소",["테마(라이트/다크) 같은 소소한 설정을 기억하기 위해 브라우저 로컬 저장소를 사용합니다. 이 데이터는 기기에만 남습니다."]),
  ("5. 아동 개인정보",["당사 도구는 범용이며 13세 미만 아동의 개인정보를 고의로 수집하지 않습니다."]),
  ("6. 방침 변경",["서비스 발전에 따라 본 방침을 업데이트할 수 있으며, 중요한 변경은 이 페이지에 날짜와 함께 표시됩니다."]),
  ("7. 문의",["궁금한 점은 " + CONTACT + " 로 연락 주세요."])]},
"zh-cn": {"title":"隐私政策","h1":"隐私政策","updated":"2026年10月2日",
 "meta":"HeicGo 隐私政策——浏览器内图像工具的数据处理方式,包括 Cookie 与第三方广告。",
 "intro":"HeicGo(“我们”)运营免费的浏览器内图像工具,包括 heicgo-ecc.pages.dev 上的 HEIC 转 JPG 转换器。本政策说明你使用我们的工具时,哪些数据会——以及不会——被收集。",
 "sections":[
  ("1. 你的照片和文件",["<b>我们不收集、存储或传输你的照片。</b>所有转换均通过 WebAssembly 在你的浏览器本地完成。文件放入工具后由你自己的设备处理,绝不上传到任何服务器。关闭或刷新页面即全部清除。"]),
  ("2. 服务器日志",["与几乎所有网站一样,我们的托管商(Cloudflare)会自动记录标准技术请求数据——IP 地址、浏览器类型、请求 URL、时间戳等——用于安全与性能目的。该数据受 <a href='https://www.cloudflare.com/privacypolicy/'>Cloudflare 隐私政策</a>约束,不用于识别个人访客。"]),
  ("3. Cookie 与广告",["我们计划投放由 Google AdSense 提供的广告。包括 Google 在内的第三方供应商会使用 Cookie,依据用户对网站的既往访问投放广告。","你可以前往 <a href='https://www.google.com/settings/ads'>Google 广告设置</a>退出个性化广告;也可以通过浏览器设置管理 Cookie——屏蔽 Cookie 不影响工具功能。"]),
  ("4. 本地存储",["我们使用浏览器本地存储记住少量偏好(如明暗主题选择)。这些数据仅保存在你的设备上,清除浏览器存储即可移除。"]),
  ("5. 儿童隐私",["我们的工具为通用型,不会有意收集 13 岁以下儿童的个人信息。"]),
  ("6. 政策变更",["服务演进时我们可能更新本政策,重大变更将在此页面反映并更新日期。"]),
  ("7. 联系我们",["对本政策有疑问?联系 " + CONTACT + "。"])]},
"zh-tw": {"title":"隱私權政策","h1":"隱私權政策","updated":"2026年10月2日",
 "meta":"HeicGo 隱私權政策——瀏覽器內圖片工具的資料處理方式,包括 Cookie 與第三方廣告。",
 "intro":"HeicGo(「我們」)營運免費的瀏覽器內圖片工具,包括 heicgo-ecc.pages.dev 上的 HEIC 轉 JPG 轉換器。本政策說明你使用我們的工具時,哪些資料會——以及不會——被收集。",
 "sections":[
  ("1. 你的照片和檔案",["<b>我們不收集、儲存或傳輸你的照片。</b>所有轉換均透過 WebAssembly 在你的瀏覽器本地完成。檔案放入工具後由你自己的裝置處理,絕不上傳到任何伺服器。關閉或重新整理頁面即全部清除。"]),
  ("2. 伺服器日誌",["與幾乎所有網站一樣,我們的代管商(Cloudflare)會自動記錄標準技術請求資料——IP 位址、瀏覽器類型、請求 URL、時間戳記等——用於安全與效能目的。該資料受 <a href='https://www.cloudflare.com/privacypolicy/'>Cloudflare 隱私權政策</a>規範,不用於識別個人訪客。"]),
  ("3. Cookie 與廣告",["我們計劃投放由 Google AdSense 提供的廣告。包括 Google 在內的第三方供應商會使用 Cookie,依據使用者對網站的既往造訪投放廣告。","你可以前往 <a href='https://www.google.com/settings/ads'>Google 廣告設定</a>退出個人化廣告;也可以透過瀏覽器設定管理 Cookie——封鎖 Cookie 不影響工具功能。"]),
  ("4. 本地儲存",["我們使用瀏覽器本地儲存記住少量偏好(如深淺色主題選擇)。這些資料僅保存在你的裝置上,清除瀏覽器儲存即可移除。"]),
  ("5. 兒童隱私",["我們的工具為通用型,不會有意收集 13 歲以下兒童的個人資料。"]),
  ("6. 政策變更",["服務演進時我們可能更新本政策,重大變更將在此頁面反映並更新日期。"]),
  ("7. 聯絡我們",["對本政策有疑問?聯絡 " + CONTACT + "。"])]},
}

ABT = {
"en": {"title":"About HeicGo — Free, Private Image Tools","h1":"About HeicGo",
 "meta":"HeicGo builds free browser-based image tools that respect your privacy. No upload, no signup, no watermark.",
 "intro":"HeicGo makes small, sharp image tools that run <b>entirely in your browser</b>. Our first tool — a HEIC to JPG converter — was born from a simple observation: hundreds of millions of iPhone photos are trapped in a format that Windows and the web still struggle to open, and most \"free\" online converters make you upload private photos to a server just to change a file format.",
 "sections":[
  ("Our principles",["<b>Privacy is the default.</b> Files are processed locally; there is no upload step to remove, because there never was one.","<b>Free means free.</b> No signup, no watermark, no daily limits, no \"premium\" unlock.","<b>Fast beats fancy.</b> One page, one job, done in seconds."]),
  ("What's next",["HeicGo currently serves 8 languages (English, German, French, Spanish, Japanese, Korean, Simplified and Traditional Chinese) and we're steadily adding tools. If an image task annoys you, chances are we're working on it."]),
  ("Contact",["Say hello or report an issue: " + CONTACT + ". We read everything."])]},
"de": {"title":"Über HeicGo","h1":"Über HeicGo",
 "meta":"HeicGo entwickelt kostenlose Bild-Tools im Browser, die Ihre Privatsphäre respektieren. Kein Upload, keine Anmeldung, kein Wasserzeichen.",
 "intro":"HeicGo baut kompakte Bild-Tools, die <b>vollständig im Browser</b> laufen. Unser erstes Werkzeug — ein HEIC-zu-JPG-Konverter — entstand aus einer einfachen Beobachtung: Hunderte Millionen iPhone-Fotos stecken in einem Format, das Windows und das Web kaum öffnen können, und die meisten „kostenlosen“ Online-Konverter verlangen das Hochladen privater Fotos auf einen Server, nur um ein Format zu ändern.",
 "sections":[
  ("Unsere Prinzipien",["<b>Privatsphäre ist Standard.</b> Dateien werden lokal verarbeitet; einen Upload-Schritt zu entfernen gibt es nicht, weil es ihn nie gab.","<b>Kostenlos heißt kostenlos.</b> Keine Anmeldung, kein Wasserzeichen, keine Tageslimits, keine versteckten Kosten.","<b>Schnell schlägt verspielt.</b> Eine Seite, eine Aufgabe, in Sekunden erledigt."]),
  ("Wie es weitergeht",["HeicGo bedient derzeit 8 Sprachen (Englisch, Deutsch, Französisch, Spanisch, Japanisch, Koreanisch, vereinfachtes und traditionelles Chinesisch) und wir bauen kontinuierlich weitere Werkzeuge. Wenn eine Bildaufgabe nervt, arbeiten wir vermutlich daran."]),
  ("Kontakt",["Schreiben Sie uns: " + CONTACT + ". Wir lesen alles."])]},
"fr": {"title":"À propos de HeicGo","h1":"À propos de HeicGo",
 "meta":"HeicGo crée des outils d'images gratuits dans le navigateur qui respectent votre vie privée. Sans téléversement, sans inscription, sans filigrane.",
 "intro":"HeicGo crée des outils d'images compacts qui fonctionnent <b>entièrement dans votre navigateur</b>. Notre premier outil — un convertisseur HEIC vers JPG — est né d'un constat simple : des centaines de millions de photos iPhone sont piégées dans un format que Windows et le web peinent à ouvrir, et la plupart des convertisseurs « gratuits » vous font téléverser des photos privées sur un serveur juste pour changer de format.",
 "sections":[
  ("Nos principes",["<b>La confidentialité par défaut.</b> Les fichiers sont traités localement ; il n'y a aucune étape de téléversement à supprimer, puisqu'elle n'a jamais existé.","<b>Gratuit veut dire gratuit.</b> Sans inscription, sans filigrane, sans limite quotidienne, sans frais cachés.","<b>La rapidité avant l'esthétique.</b> Une page, une tâche, quelques secondes."]),
  ("La suite",["HeicGo est disponible en 8 langues (anglais, allemand, français, espagnol, japonais, coréen, chinois simplifié et traditionnel) et nous ajoutons régulièrement des outils. Si une tâche image vous agace, on y travaille probablement."]),
  ("Contact",["Dites bonjour ou signalez un problème : " + CONTACT + ". Nous lisons tout."])]},
"es": {"title":"Sobre HeicGo","h1":"Sobre HeicGo",
 "meta":"HeicGo crea herramientas de imagen gratuitas en el navegador que respetan tu privacidad. Sin subida, sin registro, sin marca de agua.",
 "intro":"HeicGo crea herramientas de imagen pequeñas y precisas que funcionan <b>enteramente en tu navegador</b>. Nuestra primera herramienta — un convertidor de HEIC a JPG — nació de una observación simple: cientos de millones de fotos de iPhone quedan atrapadas en un formato que Windows y la web aún no abren, y la mayoría de convertidores «gratuitos» te hacen subir fotos privadas a un servidor solo para cambiar el formato.",
 "sections":[
  ("Nuestros principios",["<b>La privacidad por defecto.</b> Los archivos se procesan localmente; no hay paso de subida que eliminar, porque nunca existió.","<b>Gratis significa gratis.</b> Sin registro, sin marca de agua, sin límites diarios, sin «premium».","<b>La velocidad antes que la estética.</b> Una página, una tarea, segundos."]),
  ("Qué viene después",["HeicGo está disponible en 8 idiomas (inglés, alemán, francés, español, japonés, coreano, chino simplificado y tradicional) y seguimos añadiendo herramientas. Si una tarea de imágenes te molesta, probablemente estamos en ello."]),
  ("Contacto",["Saluda o reporta un problema: " + CONTACT + ". Leemos todo."])]},
"ja": {"title":"HeicGo について","h1":"HeicGo について",
 "meta":"HeicGo はプライバシーを尊重するブラウザ内画像ツールを開発しています。アップロード不要、登録不要、透かしなし。",
 "intro":"HeicGo は <b>ブラウザ内で完全に動作</b>するコンパクトな画像ツールを作っています。最初のツール — HEIC→JPG 変換 — はシンプルな観察から生まれました:数億枚の iPhone 写真が Windows やウェブが開けない形式に閉じ込められ、ほとんどの「無料」オンライン変換ツールはフォーマットを変えるだけでプライベートな写真をサーバーにアップロードさせます。",
 "sections":[
  ("私たちの原則",["<b>プライバシーはデフォルト。</b>ファイルはローカルで処理され、除外すべきアップロード工程は最初から存在しません。","<b>無料は無料。</b>登録不要、透かしなし、日制限なし、「プレミアム」解錠もなし。","<b>速さは装飾に勝る。</b>1 ページ、1 つの仕事、数秒で完了。"]),
  ("今後について",["HeicGo は現在 8 言語(英/独/仏/西/日/韓/簡体字/繁体字)に対応し、ツールを順次追加しています。画像の面倒な作業があれば、たぶん取り組んでいます。"]),
  ("お問い合わせ",["ご挨拶や不具合報告は " + CONTACT + " まで。すべて目を通します。"])]},
"ko": {"title":"HeicGo 소개","h1":"HeicGo 소개",
 "meta":"HeicGo는 개인정보를 존중하는 브라우저 기반 무료 이미지 도구를 만듭니다. 업로드 없음, 가입 없음, 워터마크 없음.",
 "intro":"HeicGo는 <b>브라우저 안에서 완전히 실행되는</b> 작고 정확한 이미지 도구를 만듭니다. 첫 도구 — HEIC→JPG 변환기 — 는 단순한 관찰에서 시작되었습니다:수억 장의 iPhone 사진이 Windows와 웹이 열지 못하는 형식에 갇혀 있고, 대부분의 「무료」 온라인 변환기는 형식 하나 바꾸는 일에 개인 사진을 서버에 업로드하라고 요구합니다.",
 "sections":[
  ("우리의 원칙",["<b>프라이버시가 기본값.</b> 파일은 로컬에서 처리되며, 제거할 업로드 단계는 애초에 존재하지 않습니다.","<b>무료는 무료.</b> 가입 없음, 워터마크 없음, 일일 제한 없음, 숨은 비용 없음.","<b>빠름이 화려함보다 낫다.</b> 한 페이지, 한 가지 작업, 몇 초면 끝."]),
  ("앞으로의 계획",["HeicGo는 현재 8개 언어(영/독/불/서/일/한/간체/번체)를 지원하며 도구를 꾸준히 추가하고 있습니다. 이미지 작업이 불편하다면 아마 우리가 다루고 있을 겁니다."]),
  ("문의",["인사나 버그 제보는 " + CONTACT + " 로. 모두 읽습니다."])]},
"zh-cn": {"title":"关于 HeicGo","h1":"关于 HeicGo",
 "meta":"HeicGo 打造尊重隐私的浏览器内免费图片工具。零上传、免注册、无水印。",
 "intro":"HeicGo 专注做<b>完全在浏览器内运行</b>的小而精的图像工具。第一个工具——HEIC 转 JPG——源于一个简单的观察:数亿张 iPhone 照片被 Windows 和互联网打不开的格式困住,而大多数「免费」在线转换器为了改个格式,要你把私密照片上传到服务器。",
 "sections":[
  ("我们的原则",["<b>隐私是默认项。</b>文件本地处理;不存在“要去掉的上传环节”,因为从来没有。","<b>免费就是免费。</b>免注册、无水印、无次数限制、没有「高级版」解锁。","<b>快比花哨重要。</b>一个页面,一件事,几秒做完。"]),
  ("接下来",["HeicGo 目前支持 8 种语言(英/德/法/西/日/韩/简中/繁中),工具在持续增加。哪件图像上的事让你烦,我们多半正在做它。"]),
  ("联系",["打招呼或报告问题:<b>liuyulong667@gmail.com</b>。每一封我们都会读。"])]},
"zh-tw": {"title":"關於 HeicGo","h1":"關於 HeicGo",
 "meta":"HeicGo 打造尊重隱私的瀏覽器內免費圖片工具。零上傳、免註冊、無浮水印。",
 "intro":"HeicGo 專注做<b>完全在瀏覽器內執行</b>的小而精的圖片工具。第一個工具——HEIC 轉 JPG——源於一個簡單的觀察:數億張 iPhone 照片被 Windows 和網際網路打不開的格式困住,而大多數「免費」線上轉換器為了改個格式,要你把私密照片上傳到伺服器。",
 "sections":[
  ("我們的原則",["<b>隱私是預設值。</b>檔案本地處理;不存在「要去掉的上傳環節」,因為從來沒有。","<b>免費就是免費。</b>免註冊、無浮水印、無次數限制、沒有「進階版」解鎖。","<b>快比花哨重要。</b>一個頁面,一件事,幾秒做完。"]),
  ("接下來",["HeicGo 目前支援 8 種語言(英/德/法/西/日/韓/簡中/繁中),工具在持續增加。哪件圖片上的事讓你煩,我們多半正在做它。"]),
  ("聯絡",["打招呼或回報問題:<b>liuyulong667@gmail.com</b>。每一封我們都會讀。"])]},
}

def build_sub(kind, code):
    t = T[code]
    d = (PRIV if kind == "privacy" else ABT)[code]
    suburl = (lambda x: "https://heicgo-ecc.pages.dev/" if x == "en"
              else f"https://heicgo-ecc.pages.dev/{kind}-{x}")
    html = BASE
    html = html.replace('<html lang="en">', f'<html lang="{code}">')
    html = html.replace('<title>HEIC to JPG Converter — Free, Private, No Upload | HeicGo</title>',
                        f'<title>{d["title"]} | HeicGo</title>')
    html = html.replace('<meta name="description" content="Convert iPhone HEIC/HEIF photos to JPG online for free. 100% private — files never leave your browser. Batch conversion, no signup, no watermark.">',
                        f'<meta name="description" content="{d["meta"]}">')
    alt = "\n".join(f'  <link rel="alternate" hreflang="{x}" href="{suburl(x)}">' for x in ORDER)
    alt += f'\n  <link rel="alternate" hreflang="x-default" href="{suburl("en")}">'
    html = html.replace('</title>', '</title>\n' + alt, 1)
    html = html.replace('__CANONICAL__', suburl(code))
    html = html.replace('__NAV_PRIVACY__', NAV[code][3]).replace('__NAV_ABOUT__', NAV[code][4])
    html = html.replace('__NAV_WHY__', NAV[code][0]).replace('__NAV_HOW__', NAV[code][1]).replace('__NAV_FAQ__', NAV[code][2])
    html = html.replace('__LANGSWITCH__', lang_switcher(code, lambda x: (kind + ("" if x == "en" else "-" + x) + ".html")))
    for a in ["why", "how", "faq"]:
        html = html.replace(f'href="#{a}"', f'href="/#{a}"')
    html = html.replace('</style>', '  .nav-links a.on { color:var(--brand); font-weight:600; }\n</style>')
    link = f'<a href="/{kind}.html">' if code == "en" else f'<a href="/{kind}-{code}.html">'
    html = html.replace(link, link.replace('<a ', '<a class="on" '))
    body = f'<h1>{d["h1"]}</h1>\n'
    if kind == "privacy":
        body += f'  <p class="updated">{d["updated"]}</p>\n'
    body += f'  <p>{d["intro"]}</p>\n'
    for h2, paras in d["sections"]:
        body += f'  <h2>{h2}</h2>\n' + "".join(f'  <p>{p}</p>\n' for p in paras)
    i, j = html.find('<h1>'), html.find('</main>')
    html = html[:i] + body + html[j:]
    html = html.replace('HeicGo — free private image tools. © 2026', t["footer"])
    return html

for code in ORDER:
    p = Path(__file__).parent / T[code]["file"]
    p.write_text(build(code), encoding="utf-8")
    print("生成:", p.name)

for code in ORDER:
    suffix = "" if code == "en" else f"-{code}"
    for kind in ["privacy", "about"]:
        p = Path(__file__).parent / f"{kind}{suffix}.html"
        p.write_text(build_sub(kind, code), encoding="utf-8")
        print("生成:", p.name)

print("完成，共", len(ORDER), "个语言页 + ", len(ORDER) * 2, "个子页")
