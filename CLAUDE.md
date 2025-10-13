# CLAUDE.md

This project contains a Docsify-based documentation site for a social cognition course, including structured summaries of academic papers.

---

## Docsify Site Structure

The documentation site lives in the `docs/` directory:

```
docs/
├── index.html              # Main HTML file with docsify configuration
├── index.md                # Homepage content
├── _sidebar.md             # Navigation sidebar
├── _navbar.md              # Top navigation bar (if used)
├── .nojekyll              # Prevents GitHub Pages from processing with Jekyll
├── glossary.md            # Course glossary
├── timeline.md            # Course timeline
└── optional-readings/     # Directory for weekly reading summaries
    ├── week-00.md
    ├── week-01.md
    ├── week-02.md
    └── week-03.md
```

### Key Files

- **index.html**: Contains all docsify configuration and loads the docsify library
- **index.md**: Homepage content (serves as README.md equivalent)
- **_sidebar.md**: Defines navigation structure in the left sidebar
- **.nojekyll**: Required for GitHub Pages deployment to skip Jekyll processing

---

## Docsify Configuration Reference

Configuration is set in `docs/index.html` within the `window.$docsify` object:

### Current Configuration

```javascript
window.$docsify = {
  name: 'PSYC137 Social Cognition',
  repo: '',
  homepage: 'index.md',
  loadNavbar: true,
  loadSidebar: true,
  subMaxLevel: 3
}
```

### Essential Configuration Options

#### Site Identity
```javascript
name: 'Site Name',              // Displayed in sidebar header
logo: '/_media/icon.svg',       // Logo in sidebar (requires name to be set)
repo: 'username/repo',          // GitHub repo link (shows corner ribbon)
nameLink: '/',                  // URL when clicking site name
```

#### Navigation & Structure
```javascript
homepage: 'index.md',           // Which file serves as homepage
loadSidebar: true,              // Enable custom sidebar from _sidebar.md
loadNavbar: true,               // Enable custom navbar from _navbar.md
hideSidebar: false,             // Completely hide sidebar
mergeNavbar: true,              // Merge navbar into sidebar on small screens
```

#### Table of Contents
```javascript
subMaxLevel: 3,                 // Show h1-h3 in sidebar TOC (0 = no TOC)
maxLevel: 4,                    // Max heading level for parsing
autoHeader: true,               // Auto-add h1 from sidebar if page lacks one
```

#### Routing & Aliases
```javascript
basePath: '/path/',             // Base path for all requests
alias: {                        // Route aliases (supports regex)
  '/.*/_sidebar.md': '/_sidebar.md',
  '/zh-cn/changelog': '/changelog'
},
routerMode: 'history',          // 'hash' (default) or 'history' mode
```

#### Features & Behavior
```javascript
auto2top: true,                 // Scroll to top on route change
executeScript: true,            // Execute scripts in markdown
coverpage: true,                // Enable cover page from _coverpage.md
notFoundPage: true,             // Enable custom 404 page
externalLinkTarget: '_blank',   // Target for external links
externalLinkRel: 'noopener',    // Rel attribute for external links
```

#### Search Plugin
```javascript
search: {
  paths: 'auto',                        // Auto-detect paths or specify array
  placeholder: 'Search',                 // Placeholder text
  noData: 'No Results!',                // No results message
  depth: 6,                             // Search heading depth
  maxAge: 86400000,                     // Cache expiration (1 day)
  hideOtherSidebarContent: false,       // Hide other sidebar content when searching
  namespace: 'website-1',               // Namespace for avoiding index collisions
  pathNamespaces: ['/zh-cn', '/ru-ru'], // Path-based namespaces for multi-language
}
```

#### Markdown Customization
```javascript
markdown: {
  smartypants: true,            // Use smart quotes
  renderer: {                   // Custom renderer functions
    code(code, lang) {
      // Custom code block rendering
      return customRender(code, lang);
    }
  }
}
```

#### Theme Customization
```javascript
themeColor: '#3F51B5',          // Primary theme color
```

---

## Common Docsify Tasks

### Adding a New Page

1. Create markdown file in `docs/` (e.g., `docs/new-page.md`)
2. Update `docs/_sidebar.md` to include link:
   ```markdown
   * [New Page](new-page.md)
   ```

### Updating Sidebar Navigation

Edit `docs/_sidebar.md`:

```markdown
* [Home](/)
* [Section 1](section1.md)
  * [Subsection 1.1](section1/sub1.md)
  * [Subsection 1.2](section1/sub2.md)
* [Section 2](section2.md)
```

**Nested sidebar structure:**
- Use indentation to create subsections
- Use section headers (without links) to organize:
  ```markdown
  * Section Header
    * [Page 1](page1.md)
    * [Page 2](page2.md)
  ```

### Custom Page Titles

Add custom title (for `<title>` tag) in sidebar link:

```markdown
* [Link Text](file.md "Custom Page Title")
```

### Enabling Plugins

Plugins are added via `<script>` tags in `index.html` after the main docsify script:

```html
<!-- Docsify core -->
<script src="//cdn.jsdelivr.net/npm/docsify@4"></script>

<!-- Search plugin -->
<script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>

<!-- Other plugins -->
<script src="//cdn.jsdelivr.net/npm/docsify-copy-code@2"></script>
```

---

## Recommended Plugins & Features

### Search Plugin (Essential)

**Add to `docs/index.html`:**

```html
<!-- In <head> or before closing </body> -->
<script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js"></script>
```

**Configure in `window.$docsify`:**

```javascript
window.$docsify = {
  search: {
    paths: 'auto',
    placeholder: 'Search',
    noData: 'No Results!',
    depth: 6,
  }
}
```

### Dark Mode Toggle

**Option 1: docsify-themeable (Recommended)**

```html
<!-- Replace theme CSS -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple.css">

<!-- Add dark theme -->
<link rel="stylesheet" media="(prefers-color-scheme: dark)" href="//cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple-dark.css">

<!-- Plugin -->
<script src="//cdn.jsdelivr.net/npm/docsify-themeable@0"></script>
```

**Option 2: docsify-darklight-theme**

```html
<!-- Themes -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify-darklight-theme@latest/dist/style.min.css">

<!-- Plugin -->
<script src="//cdn.jsdelivr.net/npm/docsify-darklight-theme@latest/dist/index.min.js"></script>
```

**Configure:**

```javascript
window.$docsify = {
  darklightTheme: {
    defaultTheme: 'light',
    dark: {
      background: '#1c2022',
      highlightColor: '#e96900',
    },
    light: {
      background: 'white',
      highlightColor: '#42b983',
    }
  }
}
```

### Cross-Linking & Auto-Glossary

**Built-in Cross-Linking:**
- Use standard markdown links: `[text](path/to/file.md)`
- Relative paths work within `docs/`
- Link to specific headings: `[text](file.md#heading-id)`

**Glossary Plugin (docsify-glossary):**

```html
<script src="//unpkg.com/docsify-glossary/dist/docsify-glossary.min.js"></script>
```

**Configure:**

```javascript
window.$docsify = {
  glossary: {
    '/': '/glossary.md',        // Path to glossary file
  }
}
```

**In glossary.md:**

```markdown
## Term Name

Definition of the term.

## Another Term

Another definition.
```

**Usage in content:**
- Use `[term](?glossary=term-name)` to auto-link to glossary
- Or just maintain manual links: `[Theory of Mind](glossary.md#theory-of-mind)`

### Other Useful Plugins

**Copy Code Button:**
```html
<script src="//cdn.jsdelivr.net/npm/docsify-copy-code@2"></script>
```

**Pagination (Previous/Next):**
```html
<script src="//cdn.jsdelivr.net/npm/docsify-pagination@2/dist/docsify-pagination.min.js"></script>
```

**Tabs:**
```html
<script src="//cdn.jsdelivr.net/npm/docsify-tabs@1"></script>
```

**Zoom Images:**
```html
<script src="//cdn.jsdelivr.net/npm/docsify@4/lib/plugins/zoom-image.min.js"></script>
```

---

## Development & Deployment

### Local Development

**Option 1: docsify-cli (Recommended)**
```bash
# Install globally
npm i docsify-cli -g

# Serve locally
docsify serve docs

# Access at http://localhost:3000
```

**Option 2: Simple Python server**
```bash
cd docs
python -m http.server 3000
```

**Option 3: VS Code Live Server**
- Install "Live Server" extension
- Right-click `docs/index.html` → "Open with Live Server"

### Deployment

**GitHub Pages:**
1. Push `docs/` to repository
2. Go to Settings → Pages
3. Select branch and `/docs` folder
4. Site will be at `https://username.github.io/repo/`

**Netlify/Vercel:**
- Set build directory to `docs`
- No build command needed (static site)

---

## Working with This Project

### Key Workflows

When updating the course site:

1. **Adding weekly readings**: Create/update files in `docs/optional-readings/`
2. **Updating navigation**: Edit `docs/_sidebar.md`
3. **Homepage changes**: Edit `docs/index.md`
4. **Glossary updates**: Edit `docs/glossary.md`
5. **Timeline updates**: Edit `docs/timeline.md`

### Testing Changes

Always test locally before deploying:
```bash
docsify serve docs
```

### Configuration Changes

All config changes go in `docs/index.html` within the `window.$docsify` object. Changes take effect immediately (refresh browser).

---

## Efficient Workflow for Formatting Tasks

### General Approach

When asked to standardize or fix formatting:

1. **Break into discrete steps** - Each type of change (citations, tags, headers, etc.) should be one step
2. **Use sub-agents for each step** - Delegate to general-purpose sub-agents to save context
3. **Have a second sub-agent verify** - Always have a separate sub-agent check the work
4. **Stage for commit after each step** - Use `git add` and `git status` after verification
5. **Wait for user approval** - User reviews and commits before proceeding to next step

### Step-by-Step Process Template

For each formatting change:

```markdown
1. DELEGATE: Launch sub-agent with clear instructions
   - Specify exact format requirements
   - Include examples
   - Ask for summary report

2. VERIFY: Launch second sub-agent to check work
   - Different agent for fresh perspective
   - Check for edge cases
   - Fix any issues found

3. STAGE: Prepare for commit
   - `git add changed/created file`
   - `git status` to confirm

4. REPORT: Summarize to user
   - What was changed
   - Number of items affected
   - Any issues found/fixed
   - Confirmation it's ready for review

5. WAIT: User commits before proceeding
```

### Why This Workflow?

- **Sub-agents save context**: Each sub-agent gets fresh context, avoiding token limitations
- **Verification catches errors**: Second pair of eyes prevents mistakes
- **Incremental commits**: Easier to review and rollback if needed
- **Clear communication**: User always knows what's happening
