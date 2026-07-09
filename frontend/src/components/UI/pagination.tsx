type Props = {
    page: number;
    pageSize: number;
    total: number;
    onPageChange: (page: number) => void;
};

export default function Pagination({
    page,
    pageSize,
    total,
    onPageChange,
}: Props) {
    const totalPages = Math.max(
        1,
        Math.ceil(total / pageSize),
    );

    const start = total === 0
        ? 0
        : (page - 1) * pageSize + 1;

    const end = Math.min(
        page * pageSize,
        total,
    );

    return (
        <div className="mt-6 flex items-center justify-between">
            <div className="text-sm text-gray-600">
                Showing {start}–{end} of {total} species
            </div>

            <div className="flex gap-2">
                <button
                    className="rounded border px-4 py-2 disabled:opacity-50"
                    disabled={page === 1}
                    onClick={() =>
                        onPageChange(page - 1)
                    }
                >
                    Previous
                </button>

                <span className="flex items-center px-3">
                    Page {page} of {totalPages}
                </span>

                <button
                    className="rounded border px-4 py-2 disabled:opacity-50"
                    disabled={page >= totalPages}
                    onClick={() =>
                        onPageChange(page + 1)
                    }
                >
                    Next
                </button>
            </div>
        </div>
    );
}