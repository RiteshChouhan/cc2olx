import xml.dom.minidom

def olx_xml(normalized):
    impl = xml.dom.minidom.getDOMImplementation()
    xml_out = impl.createDocument(None, "course", None)
    xcourse = xml_out.documentElement
    xcourse.appendChild(xml_out.createComment(" Generated by cc2olx "))
    tags = "chapter sequential vertical".split()
    _add_olx_nodes(xml_out, xcourse, normalized['children'], tags)
    return xml_out.toprettyxml()

def _add_olx_nodes(xml_out, elt, data, tags):
    if not tags:
        tags = ["xblock"]
    for dd in data:
        child = xml_out.createElement(tags[0])
        if "title" in dd:
            child.setAttribute("title", dd["title"])
        elt.appendChild(child)
        if "children" in dd:
            _add_olx_nodes(xml_out, child, dd["children"], tags[1:])

if 0:
    import StringIO
    import tarfile
    data = 'hello, world!'

    tarinfo = tarfile.TarInfo('test.txt')
    tarinfo.size = len(data)

    tar = tarfile.open('test.tar', 'a')
    tar.addfile(tarinfo, StringIO.StringIO(data))
    tar.close()