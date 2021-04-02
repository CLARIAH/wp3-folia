.. DO NOT REMOVE ANY foliaspec COMMENTS NOR EDIT THE TEXT BLOCK IMMEDIATELY FOLLOWING SUCH COMMENTS! THEY WILL BE AUTOMATICALLY UPDATED BY THE foliaspec TOOL!

.. _reference_annotation:

Reference Annotation
==================================================================

.. foliaspec:annotationtype_description(reference)
Structural annotation for referring to other annotation types. Used e.g. for referring to bibliography entries (citations) and footnotes.

Not to be confused with :ref:`coreference_annotation`!

Specification
---------------

.. foliaspec:specification(reference)
:Annotation Category: :ref:`structure_annotation_category`
:Declaration: ``<reference-annotation set="...">`` *(note: set is optional for this annotation type; if you declare this annotation type to be setless you can not assign classes)*
:Version History: Since v0.11, external references since v1.2
:**Element**: ``<ref>``
:API Class: ``Reference`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.Reference.html>`_)
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numbers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``space`` -- This attribute indicates whether spacing should be inserted after this element (it's default value is always ``yes``, so it does not need to be specified in that case), but if tokens or other structural elements are glued together then the value should be set to ``no``. This allows for reconstruction of the detokenised original text. 
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
                      * ``tag`` -- Contains a space separated list of processing tags associated with the element. A processing tag carries arbitrary user-defined information that may aid in processing a document. It may carry cues on how a specific tool should treat a specific element. The tag vocabulary is specific to the tool that processes the document. Tags carry no instrinsic meaning for the data representation and should not be used except to inform/aid processors in their task. Processors are encouraged to clean up the tags they use. Ideally, published FoLiA documents at the end of a processing pipeline carry no further tags. For encoding actual data, use ``class`` and optionally features instead.
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<alt>`` (:ref:`alternative_annotation`), ``<altlayers>`` (:ref:`alternative_annotation`), ``<comment>`` (:ref:`comment_annotation`), ``<correction>`` (:ref:`correction_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<external>`` (:ref:`external_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<br>`` (:ref:`linebreak_annotation`), ``<metric>`` (:ref:`metric_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<part>`` (:ref:`part_annotation`), ``<ph>`` (:ref:`phon_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<relation>`` (:ref:`relation_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<str>`` (:ref:`string_annotation`), ``<t>`` (:ref:`text_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<whitespace>`` (:ref:`whitespace_annotation`), ``<w>`` (:ref:`token_annotation`)
:Valid Context: ``<def>`` (:ref:`definition_annotation`), ``<div>`` (:ref:`division_annotation`), ``<event>`` (:ref:`event_annotation`), ``<ex>`` (:ref:`example_annotation`), ``<head>`` (:ref:`head_annotation`), ``<hiddenw>`` (:ref:`hiddentoken_annotation`), ``<list>`` (:ref:`list_annotation`), ``<note>`` (:ref:`note_annotation`), ``<p>`` (:ref:`paragraph_annotation`), ``<quote>`` (:ref:`quote_annotation`), ``<s>`` (:ref:`sentence_annotation`), ``<term>`` (:ref:`term_annotation`), ``<utt>`` (:ref:`utterance_annotation`), ``<w>`` (:ref:`token_annotation`)

:Extra Attributes: * ``id`` -- The ID of the element to link to
                   * ``type`` (optional) -- The type of the element that is being linked to (e.g. ``note``)

.. foliaspec:specification_element(TextMarkupReference)
:**Element**: ``<t-ref>``
:API Class: ``TextMarkupReference`` (`FoLiApy API Reference <https://foliapy.readthedocs.io/en/latest/_autosummary/folia.main.TextMarkupReference.html>`_)
:Required Attributes: 
:Optional Attributes: * ``xml:id`` -- The ID of the element; this has to be a unique in the entire document or collection of documents (corpus). All identifiers in FoLiA are of the `XML NCName <https://www.w3.org/TR/1999/WD-xmlschema-2-19990924/#NCName>`_ datatype, which roughly means it is a unique string that has to start with a letter (not a number or symbol), may contain numbers, but may never contain colons or spaces. FoLiA does not define any naming convention for IDs.
                      * ``set`` -- The set of the element, ideally a URI linking to a set definition (see :ref:`set_definitions`) or otherwise a uniquely identifying string. The ``set`` must be referred to also in the :ref:`annotation_declarations` for this annotation type.
                      * ``class`` -- The class of the annotation, i.e. the annotation tag in the vocabulary defined by ``set``.
                      * ``processor`` -- This refers to the ID of a processor in the :ref:`provenance_data`. The processor in turn defines exactly who or what was the annotator of the annotation.
                      * ``annotator`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. The annotator attribute simply refers to the name o ID of the system or human annotator that made the annotation.
                      * ``annotatortype`` -- This is an older alternative to the ``processor`` attribute, without support for full provenance. It is used together with ``annotator`` and specific the type of the annotator, either ``manual`` for human annotators or ``auto`` for automated systems.
                      * ``confidence`` -- A floating point value between zero and one; expresses the confidence the annotator places in his annotation.
                      * ``datetime`` -- The date and time when this annotation was recorded, the format is ``YYYY-MM-DDThh:mm:ss`` (note the literal T in the middle to separate date from time), as per the XSD Datetime data type.
                      * ``n`` -- A number in a sequence, corresponding to a number in the original document, for example chapter numbers, section numbers, list item numbers. This this not have to be an actual number but other sequence identifiers are also possible (think alphanumeric characters or roman numerals).
                      * ``src`` -- Points to a file or full URL of a sound or video file. This attribute is inheritable.
                      * ``begintime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the begin time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``endtime`` -- A timestamp in ``HH:MM:SS.MMM`` format, indicating the end time of the speech. If a sound clip is specified (``src``); the timestamp refers to a location in the soundclip.
                      * ``speaker`` -- A string identifying the speaker. This attribute is inheritable. Multiple speakers are not allowed, simply do not specify a speaker on a certain level if you are unable to link the speech to a specific (single) speaker.
                      * ``tag`` -- Contains a space separated list of processing tags associated with the element. A processing tag carries arbitrary user-defined information that may aid in processing a document. It may carry cues on how a specific tool should treat a specific element. The tag vocabulary is specific to the tool that processes the document. Tags carry no instrinsic meaning for the data representation and should not be used except to inform/aid processors in their task. Processors are encouraged to clean up the tags they use. Ideally, published FoLiA documents at the end of a processing pipeline carry no further tags. For encoding actual data, use ``class`` and optionally features instead.
                      * ``xlink:href`` -- Turns this element into a hyperlink to the specified URL
                      * ``xlink:type`` -- The type of link (you'll want to use ``simple`` in almost all cases).
:Accepted Data: ``<comment>`` (:ref:`comment_annotation`), ``<desc>`` (:ref:`description_annotation`), ``<br>`` (:ref:`linebreak_annotation`)
:Valid Context: 

:Extra Attributes: * ``id`` -- The ID of the element to link to
                   * ``type`` (optional) -- The type of the element that is being linked to (e.g. ``note``)

Explanation & Examples
-------------------------

FoLiA allows for things like footnotes and bibliography entry using :ref:`note_annotation`. In this section we show that
you can make references to these notes using the ``<ref>`` element, this is a structure element, which implies that the references are
explicitly present in the text. The ``<ref>`` element, however, carries an extra higher-order annotation function:

.. code-block:: xml

    <s>
      <t>We demonstrated this earlier.</t>
    </s>
    <ref id="mynote" />

Another example in tokenised data, and now we add the *optional* ``type``
attribute, which holds the type of the FoLiA element that is referred to:

.. code-block:: xml

    <s>
      <w><t>We</t></w>
      <w><t>demonstrated</t></w>
      <w><t>this</t></w>
      <w><t>earlier</t></w>
      <w><t>.</t></w>
      <ref id="mynote" type="note" />
    </s>

You can optionally make explicit the symbol used for the reference. When no
textual content is provided, whatever program renders the FoLiA document may assign its own
numbering or symbol.

.. code-block:: xml

    <s>
      <t>We demonstrated this earlier.</t>
    </s>
    <ref id="mynote" type="note"><t>1</t></ref>

This is often needed for bibliographical references:

.. code-block:: xml

    <s>
      <t>We demonstrated this earlier.</t>
    </s>
    <ref id="bib.1" type="note"><t>(van Gompel et al, 2014)</t></ref>

As a structure element, the ``<ref>`` element may contain other structure
elements such as words (:ref:`token_annotation`) or even sentences (:ref:`sentence_annotation`) or
paragraphs (:ref:`paragraph_annotation`), which can in turn contain further linguistic
annotations.

Although we framed this section in the context of notes, the ``<ref>`` element is
more general and can be used whereever you need to explicitly refer to other *structure
elements*. Common targets are figures, tables, divisions (sections, chapters,
etc).

Being a structure element, the note reference itself may carry an ID as well.
Note that the ID attribute without the xml namespace always indicates a reference
in FoLiA:

.. code-block:: xml

    <s><t>We demonstrated this earlier.</t></s>
    <ref xml:id="myreference" id="mynote" />

The difference between the reference element and the higher-order relations
(:ref:`relation_annotation`) needs to be clearly understood. Relation annotation lays
relations between annotations of any kind and thus pertain strongly to
linguistic annotation, whereas this reference element is a structural element
that is explicitly shown in the text and draws a reference that is explicitly
reflected in the text.

External references can also be made with the ``<ref>`` element, which
effectively makes it a valid tool for *hyperlinking*. This is
done by setting the ``xlink:href`` to point to the external resource and
by setting the ``format`` attribute to the format of the external
resource. The format is understood to be a MIME type and its value defaults to
``text/folia+xml``. When an external reference is made, the ``id``
attribute is optional and points to an element inside the external resource.

.. code-block:: xml

    <s>
      <w><t>We</t></w>
      <w><t>demonstrated</t></w>
      <w><t>this</t></w>
      <ref xlink:href="http://somewhere" xlink:type="simple"
        format="text/html" id="section2">
        <w><t>here</t></w>
      </ref>
      <w><t>.</t></w>
    </s>

The ``<ref>`` element has a text-markup counterpart called ``<t-ref>``, which can be used to link from untokenised text,
both for internal and external links, as shown in the next two examples:

.. code-block:: xml

    <s>
      <t>We demonstrated this earlier. <t-ref id="mynote" /></t>
    </s>

.. code-block:: xml

    <s>
      <t>We demonstrated this <t-ref xlink:href="http://somewhere" xlink:type="simple" format="text/html" id="section2">here</t-ref>.</t>
    </s>


The method of hyperlinking described in this section can be contrasted to the more generic one described in :ref:`hyperlinks`. The ``<ref>`` (and
``<t-ref>``) element offers a highly semantic way of hyperlinking, especially suited for explicitly linking to other
internal FoLiA elements, whereas the other hyperlinking method is more of a text-markup or stylistic nature and more
suited for external hyperlinks.


.. literalinclude:: ../../examples/note-reference.2.1.0.folia.xml
    :linenos:
    :language: xml


