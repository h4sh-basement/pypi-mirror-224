/* global aaIntelToolJsL10n, aaIntelToolJsOptions */

jQuery(document).ready(($) => {
    'use strict';

    const elementShipClassesAllTable = $('table.aa-intel-dscan-ship-classes-all-list');
    const elementDscanCountAll = $('span#aa-intel-dscan-all-count');
    const elementShipClassesOngridTable = $('table.aa-intel-dscan-ship-classes-ongrid-list');
    const elementDscanCountOngrid = $('span#aa-intel-dscan-ongrid-count');
    const elementShipClassesOffgridTable = $('table.aa-intel-dscan-ship-classes-offgrid-list');
    const elementDscanCountOffgrid = $('span#aa-intel-dscan-offgrid-count');
    const elementShipTypesTable = $('table.aa-intel-dscan-ship-types-list');

    /**
     * Corporation info element in datatable
     *
     * @param shipData
     * @returns {string}
     */
    const ShipInfoPanel = (shipData) => {
        let html_logo = '' +
            '<span class="aa-intel-ship-image-wrapper">\n' +
            '    <img ' +
            '        class="eve-image" ' +
            '        data-eveid="' + shipData['id'] + '" ' +
            '        src="' + shipData['image'] + '" ' +
            '        alt="' + shipData['name'] + '" ' +
            '        title="' + shipData['name'] + '" ' +
            '        width="32" ' +
            '        height="32">\n' +
            '</span>';

        let html_info = '' +
            '<span class="aa-intel-ship-information-wrapper">\n' +
            '    <span class="aa-intel-ship-name-wrapper">\n' +
            '        ' + shipData['name'] + '\n' +
            '    </span>\n' +
            '</span>\n';

        return html_logo + html_info;
    };

    /**
     * Datatable D-Scan All
     */
    elementShipClassesAllTable.DataTable({
        paging: false,
        language: aaIntelToolJsL10n.dataTables.translation,
        lengthChange: false,
        dom:
            '<\'row\'<\'col-sm-12\'f>>' +
            '<\'row\'<\'col-sm-12\'tr>>' +
            '<\'row\'<\'col-sm-12\'i>>',
        ajax: {
            url: aaIntelToolJsOptions.ajax.getShipClassesAll,
            dataSrc: '',
            cache: true
        },
        columns: [
            {
                data: (data) => {
                    return ShipInfoPanel(data);
                }
            },
            {
                data: 'count'
            },
            {
                data: 'type_name'
            }
        ],
        order: [
            [1, 'desc']
        ],
        columnDefs: [
            {
                targets: 0,
                createdCell: (td) => {
                    $(td).addClass('text-ellipsis');
                }
            },
            {
                targets: 1,
                width: 45,
                createdCell: (td) => {
                    $(td).addClass('text-right');
                }
            },
            {
                targets: 2,
                visible: false
            }
        ],
        createdRow: (row, data) => {
            // D-Scan total count
            const currentTotal = elementDscanCountAll.html();
            const newTotal = parseInt(currentTotal) + data['count'];

            elementDscanCountAll.html(newTotal);

            $(row).attr('data-highlight', `shiptype-${data['type_name_sanitised']}`);

            // Highlight
            $(row).on('mouseenter', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .addClass('aa-intel-highlight');
            }).on('mouseleave', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .removeClass('aa-intel-highlight');
            });

            // Sticky
            $(row).on('click', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .toggleClass('aa-intel-highlight-sticky');
            }).on('click', '.aa-intel-information-link', (e) => {
                e.stopPropagation();
            });
        }
    });


    /**
     * Datatable D-Scan On Grid
     */
    elementShipClassesOngridTable.DataTable({
        paging: false,
        language: aaIntelToolJsL10n.dataTables.translation,
        lengthChange: false,
        dom:
            '<\'row\'<\'col-sm-12\'f>>' +
            '<\'row\'<\'col-sm-12\'tr>>' +
            '<\'row\'<\'col-sm-12\'i>>',
        ajax: {
            url: aaIntelToolJsOptions.ajax.getShipClassesOngrid,
            dataSrc: '',
            cache: true
        },
        columns: [
            {
                data: (data) => {
                    return ShipInfoPanel(data);
                }
            },
            {
                data: 'count'
            },
            {
                data: 'type_name'
            }
        ],
        order: [
            [1, 'desc']
        ],
        columnDefs: [
            {
                targets: 0,
                createdCell: (td) => {
                    $(td).addClass('text-ellipsis');
                }
            },
            {
                targets: 1,
                width: 45,
                createdCell: (td) => {
                    $(td).addClass('text-right');
                }
            },
            {
                targets: 2,
                visible: false
            }
        ],
        createdRow: (row, data) => {
            // D-Scan total count
            const currentTotal = elementDscanCountOngrid.html();
            const newTotal = parseInt(currentTotal) + data['count'];

            elementDscanCountOngrid.html(newTotal);

            $(row).attr('data-highlight', `shiptype-${data['type_name_sanitised']}`);

            // Highlight
            $(row).on('mouseenter', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .addClass('aa-intel-highlight');
            }).on('mouseleave', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .removeClass('aa-intel-highlight');
            });

            // Sticky
            $(row).on('click', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .toggleClass('aa-intel-highlight-sticky');
            }).on('click', '.aa-intel-information-link', (e) => {
                e.stopPropagation();
            });
        }
    });


    /**
     * Datatable D-Scan Off Grid
     */
    elementShipClassesOffgridTable.DataTable({
        paging: false,
        language: aaIntelToolJsL10n.dataTables.translation,
        lengthChange: false,
        dom:
            '<\'row\'<\'col-sm-12\'f>>' +
            '<\'row\'<\'col-sm-12\'tr>>' +
            '<\'row\'<\'col-sm-12\'i>>',
        ajax: {
            url: aaIntelToolJsOptions.ajax.getShipClassesOffgrid,
            dataSrc: '',
            cache: true
        },
        columns: [
            {
                data: (data) => {
                    return ShipInfoPanel(data);
                }
            },
            {
                data: 'count'
            },
            {
                data: 'type_name'
            }
        ],
        order: [
            [1, 'desc']
        ],
        columnDefs: [
            {
                targets: 0,
                createdCell: (td) => {
                    $(td).addClass('text-ellipsis');
                }
            },
            {
                targets: 1,
                width: 45,
                createdCell: (td) => {
                    $(td).addClass('text-right');
                }
            },
            {
                targets: 2,
                visible: false
            }
        ],
        createdRow: (row, data) => {
            // D-Scan total count
            const currentTotal = elementDscanCountOffgrid.html();
            const newTotal = parseInt(currentTotal) + data['count'];

            elementDscanCountOffgrid.html(newTotal);

            $(row).attr('data-highlight', `shiptype-${data['type_name_sanitised']}`);

            // Highlight
            $(row).on('mouseenter', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .addClass('aa-intel-highlight');
            }).on('mouseleave', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .removeClass('aa-intel-highlight');
            });

            // Sticky
            $(row).on('click', () => {
                $(`tr[data-highlight="shiptype-${data['type_name_sanitised']}"]`)
                    .toggleClass('aa-intel-highlight-sticky');
            }).on('click', '.aa-intel-information-link', (e) => {
                e.stopPropagation();
            });
        }
    });


    /**
     * Datatable D-Scan Off Grid
     */
    elementShipTypesTable.DataTable({
        paging: false,
        language: aaIntelToolJsL10n.dataTables.translation,
        lengthChange: false,
        dom:
            '<\'row\'<\'col-sm-12\'f>>' +
            '<\'row\'<\'col-sm-12\'tr>>' +
            '<\'row\'<\'col-sm-12\'i>>',
        ajax: {
            url: aaIntelToolJsOptions.ajax.getShipTypes,
            dataSrc: '',
            cache: true
        },
        columns: [
            {
                data: 'name'
            },
            {
                data: 'count'
            }
        ],
        order: [
            [1, 'desc']
        ],
        columnDefs: [
            {
                targets: 1,
                width: 45,
                createdCell: (td) => {
                    $(td).addClass('text-right');
                }
            }
        ],
        createdRow: (row, data) => {
            $(row).attr('data-highlight', `shiptype-${data['name_sanitised']}`);

            // Highlight
            $(row).on('mouseenter', () => {
                $(`tr[data-highlight="shiptype-${data['name_sanitised']}"]`)
                    .addClass('aa-intel-highlight');
            }).on('mouseleave', () => {
                $(`tr[data-highlight="shiptype-${data['name_sanitised']}"]`)
                    .removeClass('aa-intel-highlight');
            });

            // Sticky
            $(row).on('click', () => {
                $(`tr[data-highlight="shiptype-${data['name_sanitised']}"]`)
                    .toggleClass('aa-intel-highlight-sticky');
            }).on('click', '.aa-intel-information-link', (e) => {
                e.stopPropagation();
            });
        }
    });
});
