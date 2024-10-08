## Привязка окна игры в режиме OCR

По умолчанию активирована опция `Автоматическая привязка окна после выбора области OCR`. Когда все четыре угла рамки области принадлежат одному окну HWND, она автоматически привязывается к этому окну.

Как правило, при использовании других программ OCR одна из раздражающих вещей заключается в том, что часто нужно следить за положением окна игры и окна перевода. Возможно, окно перевода и область скриншота пересекаются, или иногда окно игры нужно переместить на задний план, что тоже раздражает.

Однако, настройка **привязки окна** в Luna идеально решает эту проблему.

Нажмите кнопку **привязки окна**, затем нажмите на окно игры, кнопка станет розовой, что указывает на успешную привязку окна игры.

![img](https://image.lunatranslator.org/zh/gooduseocr/bind.png)

![img](https://image.lunatranslator.org/zh/gooduseocr/bindok.png)

Это приведет к некоторым важным изменениям:

1. **Скриншот будет делаться только окну игры, не будут захвачены другие окна**. Таким образом, окно перевода можно разместить в любом месте, не беспокоясь о том, что оно пересекается с областью скриншота и вызывает резкие изменения; таким образом, когда окно игры закрыто другим окном, скриншот будет делаться только окну игры, не захватывая закрывающее окно.

2. **Когда окно игры перемещается, область OCR будет следовать за окном игры синхронно**. Таким образом, когда иногда нужно переместить окно игры, не нужно перемещать рамку области OCR, особенно когда рамка области скрыта, не нужно показывать-перемещать-скрывать.

Кроме того, после привязки окна игры есть и другие преимущества:

1. Функция скриншота игры может более точно захватывать окно игры.

2. Функция отслеживания времени игры может более точно записывать время.

3. Можно использовать встроенный Magpie или вызывать загруженный вами Magpie с помощью кнопки инструмента.

4. Можно получить местоположение игры и внутренний ID программы из дескриптора окна, что позволяет настроить игру, включая настройки языка/синтеза речи/оптимизации перевода/обработки текста/Anki и т.д. специально для этой игры.

А также некоторые другие оптимизации, которые не помню, требуют привязки окна для использования.

Таким образом, даже если привязано окно игры и используется только OCR без HOOK, на самом деле можно получить лучший опыт, чем с другими программами.