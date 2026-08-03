(() => {
    const DRAWER_STYLE_ID = 'cent-prd-drawer-style';
    const DRAWER_ROOT_ID = 'cent-prd-drawer-root';

    function ensureStyles() {
        if (document.getElementById(DRAWER_STYLE_ID)) {
            return;
        }

        const style = document.createElement('style');
        style.id = DRAWER_STYLE_ID;
        style.textContent = `
            .prd-drawer-overlay {
                position: fixed;
                inset: 0;
                background: rgba(15, 23, 42, 0.38);
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.25s ease;
                z-index: 2000;
            }
            .prd-drawer-overlay.is-open {
                opacity: 1;
                pointer-events: auto;
            }
            .prd-drawer-panel {
                position: absolute;
                right: 0;
                top: 0;
                bottom: 0;
                width: min(960px, 82vw);
                background: #ffffff;
                box-shadow: 24px 0 48px rgba(15, 23, 42, 0.18);
                transform: translateX(100%);
                transition: transform 0.25s ease;
                display: flex;
                flex-direction: column;
            }
            .prd-drawer-overlay.is-open .prd-drawer-panel {
                transform: translateX(0);
            }
            .prd-drawer-header {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 12px;
                padding: 18px 20px;
                border-bottom: 1px solid #e5e7eb;
                background: #ffffff;
            }
            .prd-drawer-title {
                font-size: 16px;
                font-weight: 600;
                color: #111827;
            }
            .prd-drawer-close {
                width: 32px;
                height: 32px;
                border-radius: 9999px;
                border: 1px solid #e5e7eb;
                background: #ffffff;
                color: #6b7280;
                cursor: pointer;
                transition: all 0.2s ease;
            }
            .prd-drawer-close:hover {
                background: #f9fafb;
                color: #111827;
            }
            .prd-drawer-body {
                flex: 1;
                background: #f3f4f6;
            }
            .prd-drawer-iframe {
                width: 100%;
                height: 100%;
                border: 0;
                background: #ffffff;
            }
            body.prd-drawer-open {
                overflow: hidden;
            }
            @media (max-width: 768px) {
                .prd-drawer-panel {
                    width: 100vw;
                }
            }
        `;
        document.head.appendChild(style);
    }

    function ensureDrawer() {
        let root = document.getElementById(DRAWER_ROOT_ID);
        if (root) {
            return root;
        }

        root = document.createElement('div');
        root.id = DRAWER_ROOT_ID;
        root.className = 'prd-drawer-overlay';
        root.innerHTML = `
            <div class="prd-drawer-panel" role="dialog" aria-modal="true" aria-label="页面PRD">
                <div class="prd-drawer-header">
                    <div class="prd-drawer-title">页面PRD</div>
                    <button type="button" class="prd-drawer-close" aria-label="关闭页面PRD">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div class="prd-drawer-body">
                    <iframe class="prd-drawer-iframe" title="页面PRD"></iframe>
                </div>
            </div>
        `;

        document.body.appendChild(root);

        root.addEventListener('click', (event) => {
            if (event.target === root) {
                closeDrawer();
            }
        });

        root.querySelector('.prd-drawer-close').addEventListener('click', closeDrawer);

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape' && root.classList.contains('is-open')) {
                closeDrawer();
            }
        });

        return root;
    }

    function openDrawer(url, title) {
        const root = ensureDrawer();
        const iframe = root.querySelector('.prd-drawer-iframe');
        const titleNode = root.querySelector('.prd-drawer-title');

        iframe.src = url;
        titleNode.textContent = title || '页面PRD';
        root.classList.add('is-open');
        document.body.classList.add('prd-drawer-open');
    }

    function closeDrawer() {
        const root = document.getElementById(DRAWER_ROOT_ID);
        if (!root) {
            return;
        }

        root.classList.remove('is-open');
        document.body.classList.remove('prd-drawer-open');
    }

    function bindDrawerLinks() {
        document.querySelectorAll('[data-prd-drawer]').forEach((link) => {
            link.addEventListener('click', (event) => {
                event.preventDefault();
                openDrawer(
                    link.getAttribute('href'),
                    link.getAttribute('data-prd-title') || link.textContent.trim() || '页面PRD'
                );
            });
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        ensureStyles();
        ensureDrawer();
        bindDrawerLinks();
    });
})();
