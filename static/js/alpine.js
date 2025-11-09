// This file is intentionally left empty as we're using the CDN version of Alpine.js
// The CDN version is included in the base template for better performance
// You can add custom Alpine.js components here if needed
// For example:
/*
document.addEventListener('alpine:init', () => {
    Alpine.data('problemFilter', () => ({
        difficulty: 'all',
        language: 'all',
        tag: 'all',
        
        applyFilters() {
            // Apply filters to problem list
            const params = new URLSearchParams();
            if (this.difficulty !== 'all') params.append('difficulty', this.difficulty);
            if (this.language !== 'all') params.append('language', this.language);
            if (this.tag !== 'all') params.append('tag', this.tag);
            
            window.location.search = params.toString();
        }
    }));
});
*/