// Initialize DataTables on all tables when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    // Wait a bit to ensure tables from CSV are rendered
    setTimeout(function() {
        // Find all tables in the document
        const tables = document.querySelectorAll('table');

        tables.forEach(function(table, index) {
            // Skip if already initialized
            if (table.classList.contains('dataTable')) {
                return;
            }

            // Add an ID if it doesn't have one
            if (!table.id) {
                table.id = 'datatable-' + index;
            }

            // Initialize DataTable with export buttons
            try {
                $('#' + table.id).DataTable({
                    dom: 'Bfrtip',
                    buttons: [
                        {
                            extend: 'csvHtml5',
                            text: 'Export CSV',
                            className: 'btn-export'
                        },
                        {
                            extend: 'excelHtml5',
                            text: 'Export Excel',
                            className: 'btn-export'
                        }
                    ],
                    pageLength: 25,
                    lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
                    order: [], // No default sorting
                    responsive: true,
                    autoWidth: false,
                    columnDefs: [
                        {
                            targets: '_all',
                            className: 'dt-body-left dt-head-left'
                        }
                    ]
                });
            } catch (e) {
                console.error('Error initializing DataTable for table ' + table.id + ':', e);
            }
        });
    }, 500); // Wait 500ms for CSV tables to render
});
