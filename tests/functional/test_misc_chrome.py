import os
import logging

from thug.ThugAPI.ThugAPI import ThugAPI

log = logging.getLogger("Thug")


class TestMiscSamplesChrome(object):
    thug_path = os.path.dirname(os.path.realpath(__file__)).split("thug")[0]
    misc_path = os.path.join(thug_path, "thug", "samples/misc")

    def do_perform_test(self, caplog, sample, expected):
        thug = ThugAPI()

        thug.set_useragent('win7chrome49')
        thug.set_events('click,storage')
        thug.disable_cert_logging()
        thug.set_features_logging()
        thug.log_init(sample)
        thug.run_local(sample)

        records = [r.message for r in caplog.records]

        matches = 0

        for e in expected:
            for record in records:
                if e in record:
                    matches += 1

        assert matches >= len(expected)

    def test_plugindetect1(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.6.html")
        expected = ['AdobeReader version: 9.1.0.0',
                    'Flash version: 10.0.64.0']

        self.do_perform_test(caplog, sample, expected)

    def test_plugindetect2(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.8.html")
        expected = ['AdobeReader version: 9,1,0,0',
                    'Flash version: 10,0,64,0',
                    'Java version: 1,6,0,32']

        self.do_perform_test(caplog, sample, expected)

    def test_test1(self, caplog):
        sample   = os.path.join(self.misc_path, "test1.html")
        expected = ['[Window] Alert Text: one']
        self.do_perform_test(caplog, sample, expected)

    def test_test2(self, caplog):
        sample   = os.path.join(self.misc_path, "test2.html")
        expected = ['[Window] Alert Text: Java enabled: true']
        self.do_perform_test(caplog, sample, expected)

    def test_test3(self, caplog):
        sample   = os.path.join(self.misc_path, "test3.html")
        expected = ['[Window] Alert Text: foo']
        self.do_perform_test(caplog, sample, expected)

    def test_testAppendChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testAppendChild.html")
        expected = ['Don\'t care about me',
                    'Just a sample',
                    'Attempt to append a null element failed',
                    'Attempt to append an invalid element failed',
                    'Attempt to append a text element failed',
                    'Attempt to append a read-only element failed']

        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode.html")
        expected = ['<div id="cloned"><q>Can you copy <em>everything</em> I say?</q></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode2.html")
        expected = ['[Window] Alert Text: [object HTMLButtonElement]',
                    '[Window] Alert Text: Clone node',
                    '[Window] Alert Text: None',
                    '[Window] Alert Text: [object Attr]',
                    '[Window] Alert Text: True']

        self.do_perform_test(caplog, sample, expected)

    def test_testCreateHTMLDocument(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateHTMLDocument.html")
        expected = ['[object HTMLDocument]',
                    '[object HTMLBodyElement]',
                    '<p>This is a new paragraph.</p>']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentAll(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentAll.html")
        expected = ['http://www.google.com']
        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentWrite1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentWrite1.html")
        expected = ['Foobar',
                    "Google</a><script>alert('foobar');</script><script language=\"VBScript\">alert('Gnam');</script><script>alert('Aieeeeee');</script></body>"]
        self.do_perform_test(caplog, sample, expected)

    def test_testExternalSidebar(self, caplog):
        sample   = os.path.join(self.misc_path, "testExternalSidebar.html")
        expected = ['[Window] Alert Text: Internet Explorer >= 7.0 or Chrome']
        self.do_perform_test(caplog, sample, expected)

    def test_testGetElementsByClassName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByClassName.html")
        expected = ['First',
                    'Hello World!',
                    'Second']
        self.do_perform_test(caplog, sample, expected)

    def test_testInnerHTML(self, caplog):
        sample   = os.path.join(self.misc_path, "testInnerHTML.html")
        expected = ['dude', 'Fred Flinstone']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertBefore(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertBefore.html")
        expected = ["<div>Just a sample</div><div>I'm your reference!</div></body></html>",
                    "[ERROR] Attempting to insert null element",
                    "[ERROR] Attempting to insert an invalid element",
                    "[ERROR] Attempting to insert using an invalid reference element",
                    "[ERROR] Attempting to insert a text node using an invalid reference element"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocalStorage(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocalStorage.html")
        expected = ["Alert Text: Fired",
                    "Alert Text: bar",
                    "Alert Text: south"]
        self.do_perform_test(caplog, sample, expected)

    def test_testPlugins(self, caplog):
        sample   = os.path.join(self.misc_path, "testPlugins.html")
        expected = ["Shockwave Flash 10.0.64.0",
                    "Windows Media Player 7",
                    "Adobe Acrobat"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode.html")
        expected = ["thelink",
                    "thediv"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode2.html")
        expected = ["thelink",
                    "thediv2"]
        self.do_perform_test(caplog, sample, expected)

    def test_testQuerySelector(self, caplog):
        sample   = os.path.join(self.misc_path, "testQuerySelector.html")
        expected = ["Alert Text: Have a Good life.",
                    "CoursesWeb.net"]
        self.do_perform_test(caplog, sample, expected)

    def test_testQuerySelector2(self, caplog):
        sample   = os.path.join(self.misc_path, "testQuerySelector2.html")
        expected = ['CoursesWeb.net',
                    "MarPlo.net",
                    'php.net']
        self.do_perform_test(caplog, sample, expected)

    def test_testScope(self, caplog):
        sample   = os.path.join(self.misc_path, "testScope.html")
        expected = ["foobar",
                    "foo",
                    "bar",
                    "True",
                    "3",
                    "2012-10-07 11:13:00",
                    "3.14159265359",
                    "/foo/i"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSessionStorage(self, caplog):
        sample   = os.path.join(self.misc_path, "testSessionStorage.html")
        expected = ["key1",
                    "key2",
                    "value1",
                    "value3"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSetInterval(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetInterval.html")
        expected = ["[Window] Alert Text: Hello"]
        self.do_perform_test(caplog, sample, expected)

    def test_testText(self, caplog):
        sample   = os.path.join(self.misc_path, "testText.html")
        expected = ['<p id="p1">First line of paragraph.<br/> Some text added dynamically. </p>']
        self.do_perform_test(caplog, sample, expected)

    def test_testWindowOnload(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindowOnload.html")
        expected = ["[Window] Alert Text: Fired"]
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML1(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML1.html")
        expected = ['<div id="five">five</div><div id="one">one</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML2(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML2.html")
        expected = ['<div id="two"><div id="six">six</div>two</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML3(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML3.html")
        expected = ['<div id="three">three<div id="seven">seven</div></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML4(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML4.html")
        expected = ['<div id="four">four</div><div id="eight">eight</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testCurrentScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testCurrentScript.html")
        expected = ["[Window] Alert Text: This page has scripts",
                    "[Window] Alert Text: text/javascript",
                    "[Window] Alert Text: Just a useless script"]
        self.do_perform_test(caplog, sample, expected)

    def test_testChrome(self, caplog):
        sample   = os.path.join(self.misc_path, "testChrome.html")
        expected = ["[Window] Alert Text: [object Object]", ]
        self.do_perform_test(caplog, sample, expected)

    def test_testTextNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextNode.html")
        expected = ['nodeName: #text',
                    'nodeType: 3',
                    'Object: [object Text]',
                    'nodeValue: Hello World',
                    'Length: 11',
                    'Substring(2,5): llo W',
                    'New nodeValue (replace): HelloAWorld',
                    'New nodeValue (delete 1): HelloWorld',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): Hello',
                    'New nodeValue (append): Hello Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): Hello New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testCommentNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCommentNode.html")
        expected = ['nodeName: #comment',
                    'nodeType: 8',
                    'Object: [object Comment]',
                    'nodeValue: <!--Hello World-->',
                    'Length: 18',
                    'Substring(2,5): --Hel',
                    'New nodeValue (replace): <!--HAllo World-->',
                    'New nodeValue (delete 1): <!--Hllo World-->',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): <!--H',
                    'New nodeValue (append): <!--H Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): <!--H New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testDOMImplementation(self, caplog):
        sample   = os.path.join(self.misc_path, "testDOMImplementation.html")
        expected = ["hasFeature('core'): true", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testAttrNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testAttrNode.html")
        expected = ['Object: [object Attr]',
                    'nodeName: test',
                    'nodeType: 2',
                    'nodeValue: foo',
                    'Length: undefined',
                    'New nodeValue: test2',
                    'Parent: null',
                    'Owner: null',
                    'Name: test',
                    'Specified: true',
                    'childNodes length: 0']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild.html")
        expected = ['innerText: Old child',
                    '[ERROR] Attempting to replace with a null element',
                    '[ERROR] Attempting to replace a null element',
                    '[ERROR] Attempting to replace with an invalid element',
                    '[ERROR] Attempting to replace an invalid element',
                    '[ERROR] Attempting to replace on a read-only element failed',
                    'Alert Text: New child',
                    '<div id="foobar"><!--Just a comment--></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testCookie(self, caplog):
        sample   = os.path.join(self.misc_path, "testCookie.html")
        expected = ["Alert Text: favorite_food=tripe; name=oeschger", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment1.html")
        expected = ["<div><p>Test</p></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment2(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment2.html")
        expected = ["<div id=\"foobar\"><b>This is B</b></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment3(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment3.html")
        expected = ["foo:bar", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testClassList2(self, caplog):
        sample   = os.path.join(self.misc_path, "testClassList2.html")
        expected = ['[Initial value] <div class="foo"></div>',
                    '[After remove and add] <div class="anotherclass"></div>',
                    '[Item] anotherclass',
                    '[Empty item] null',
                    '[Toggle visible] true',
                    '[After multiple adds] <div class="anotherclass visible foo bar baz"></div>',
                    '[After multiple removes] <div class="anotherclass visible"></div>',
                    '[After replace] <div class="visible justanotherclass"></div>',
                    '[After toggle] <div class="justanotherclass"></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testClassList4(self, caplog):
        sample   = os.path.join(self.misc_path, "testClassList4.html")
        expected = ['[After remove and add] <div class="anotherclass"></div>', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentType(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentType.html")
        expected = ['Doctype: [object DocumentType]',
                    'Doctype name: html',
                    'Doctype nodeName: html',
                    'Doctype nodeType: 10',
                    'Doctype nodeValue: null',
                    'Doctype publicId: ',
                    'Doctype systemId: ',
                    'Doctype textContent: null']

        self.do_perform_test(caplog, sample, expected)

    def test_testRemoveChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testRemoveChild.html")
        expected = ['<div>Don\'t care about me</div>',
                    '[ERROR] Attempting to remove null element',
                    '[ERROR] Attempting to remove an invalid element',
                    '[ERROR] Attempting to remove a read-only element',
                    '[ERROR] Attempting to remove an element not in the tree',
                    '[ERROR] Attempting to remove from a read-only element']

        self.do_perform_test(caplog, sample, expected)

    def test_testNamedNodeMap(self, caplog):
        sample   = os.path.join(self.misc_path, "testNamedNodeMap.html")
        expected = ['hasAttributes (before removal): true',
                    'hasAttribute(\'id\'): true',
                    'First test: id->p1',
                    'Second test: id->p1',
                    'Third test: id->p1',
                    'Fourth test: id->p1',
                    'Fifth test failed',
                    'Not existing: null',
                    'hasAttributes (after removal): false',
                    'Sixth test: foo->bar',
                    'Seventh test: foo->bar2',
                    'Final attributes length: 1']

        self.do_perform_test(caplog, sample, expected)

    def test_testEntityReference(self, caplog):
        sample   = os.path.join(self.misc_path, "testEntityReference.html")
        expected = ['node: [object EntityReference]',
                    'name: &',
                    'nodeName: &',
                    'nodeType: 5',
                    'nodeValue: null']

        self.do_perform_test(caplog, sample, expected)

    def test_getElementsByTagName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByTagName.html")
        expected = ['[object HTMLHtmlElement]',
                    '[object HTMLHeadElement]',
                    '[object HTMLBodyElement]',
                    '[object HTMLParagraphElement]',
                    '[object HTMLScriptElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_getElementsByTagName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByTagName.html")
        expected = ['[object HTMLHtmlElement]',
                    '[object HTMLHeadElement]',
                    '[object HTMLBodyElement]',
                    '[object HTMLParagraphElement]',
                    '[object HTMLScriptElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentElement.html")
        expected = ['<a href="http://www.google.com">Google</a>']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute1(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute1.html")
        expected = ['Attribute: bar',
                    'Attribute (after removal): null']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute2(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute2.html")
        expected = ['[element workaround redirection] about:blank -> https://buffer.github.io/thug/notexists.html',
                    '[element workaround redirection] about:blank -> https://buffer.github.io/thug/']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute3(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute3.html")
        expected = ['Alert Text: foo',
                    'Alert Text: bar',
                    'Alert Text: test',
                    'Alert Text: foobar']

        self.do_perform_test(caplog, sample, expected)

    def test_testCDATASection(self, caplog):
        sample   = os.path.join(self.misc_path, "testCDATASection.html")
        expected = ['nodeName: #cdata-section',
                    'nodeType: 4',
                    '<xml>&lt;![CDATA[Some &lt;CDATA&gt; data &amp; then some]]&gt;</xml>']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLCollection.html")
        expected = ['<div id="odiv1">Page one</div>',
                    '<div name="odiv2">Page two</div>']

        self.do_perform_test(caplog, sample, expected)


    def test_testProcessingInstruction(self, caplog):
        sample   = os.path.join(self.misc_path, "testProcessingInstruction.html")
        expected = ['[object ProcessingInstruction]',
                    'nodeName: xml-stylesheet',
                    'nodeType: 7',
                    'nodeValue: href="mycss.css" type="text/css"',
                    'target: xml-stylesheet']

        self.do_perform_test(caplog, sample, expected)

    def test_testWindow(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindow.html")
        expected = ['window: [object Window]',
                    'self: [object Window]',
                    'top: [object Window]',
                    'length: 0',
                    'history: [object History]',
                    'pageXOffset: 0',
                    'pageYOffset: 0',
                    'screen: [object Screen]',
                    'screenLeft: 0',
                    'screenX: 0',
                    'confirm: true']

        self.do_perform_test(caplog, sample, expected)
