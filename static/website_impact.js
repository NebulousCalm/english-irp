const get_website_api = async (url) => {
    try {
        const response = await fetch(`https://api.websitecarbon.com/site?url=${url}`);
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
            const requirements = await response.json();
        } catch (error) {
        console.error('Error fetching API:', error.message);
    }
};

get_website_api('https://english-irp.vercel.app');
