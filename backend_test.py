#!/usr/bin/env python3
"""
Backend API Test Suite for CMC Portfolio
Tests all HTML page endpoints and static file serving
"""

import requests
import sys
from datetime import datetime

class CMCPortfolioTester:
    def __init__(self, base_url="https://cmc-portfolio.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status=200, expected_content_type=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, timeout=10)
            else:
                raise ValueError(f"Unsupported method: {method}")

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                
                # Check content type if specified
                if expected_content_type:
                    content_type = response.headers.get('content-type', '').lower()
                    if expected_content_type.lower() in content_type:
                        print(f"✅ Content-Type: {content_type}")
                    else:
                        print(f"⚠️  Content-Type mismatch - Expected: {expected_content_type}, Got: {content_type}")
                        
                # Check content length
                content_length = len(response.text)
                print(f"   Content Length: {content_length} chars")
                
                return True, response
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text[:200]}...")
                self.failed_tests.append({
                    'name': name,
                    'endpoint': endpoint,
                    'expected': expected_status,
                    'actual': response.status_code,
                    'error': response.text[:200]
                })
                return False, response

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append({
                'name': name,
                'endpoint': endpoint,
                'expected': expected_status,
                'actual': 'ERROR',
                'error': str(e)
            })
            return False, None

    def test_health_check(self):
        """Test health check endpoint"""
        return self.run_test("Health Check", "GET", "api/health", 200)

    def test_html_pages(self):
        """Test all HTML pages"""
        pages = [
            ("Home Page", "api/site/index.html"),
            ("Chi Sono Page", "api/site/chi-sono.html"),
            ("Progetti Page", "api/site/progetti.html"),
            ("CV Page", "api/site/cv.html"),
            ("Contatti Page", "api/site/contatti.html"),
        ]
        
        results = []
        for name, endpoint in pages:
            success, response = self.run_test(name, "GET", endpoint, 200, "text/html")
            results.append((name, success, response))
            
            # Verify it's actually HTML content
            if success and response:
                content = response.text.lower()
                if '<html' in content and '</html>' in content:
                    print(f"   ✅ Valid HTML structure detected")
                else:
                    print(f"   ⚠️  Possibly invalid HTML structure")
                    
                # Check for key elements
                if 'martina caputo' in content:
                    print(f"   ✅ Contains expected content")
                else:
                    print(f"   ⚠️  Missing expected content")
        
        return results

    def test_static_assets(self):
        """Test static asset serving"""
        assets = [
            ("Main CSS", "api/site/css/styles.css", "text/css"),
            ("Main JS", "api/site/js/main.js", "application/javascript"),
            ("Logo SVG", "api/site/images/logo-cmc.svg", "image/svg+xml"),
            ("CV PDF", "api/site/assets/cv.pdf", "application/pdf"),
        ]
        
        results = []
        for name, endpoint, content_type in assets:
            success, response = self.run_test(name, "GET", endpoint, 200, content_type)
            results.append((name, success))
            
        return results

    def print_summary(self):
        """Print test summary"""
        print(f"\n" + "="*60)
        print(f"🏁 TEST SUMMARY")
        print(f"="*60)
        print(f"📊 Tests Run: {self.tests_run}")
        print(f"✅ Tests Passed: {self.tests_passed}")
        print(f"❌ Tests Failed: {self.tests_run - self.tests_passed}")
        print(f"📈 Success Rate: {(self.tests_passed/self.tests_run)*100:.1f}%")
        
        if self.failed_tests:
            print(f"\n❌ FAILED TESTS:")
            for test in self.failed_tests:
                print(f"   • {test['name']}: {test['error']}")
        
        print(f"\n🕒 Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        return self.tests_passed == self.tests_run

def main():
    print("🚀 Starting CMC Portfolio Backend Test Suite")
    print(f"🕒 Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tester = CMCPortfolioTester()
    
    # Run all tests
    print("\n" + "="*60)
    print("TESTING API HEALTH")
    print("="*60)
    tester.test_health_check()
    
    print("\n" + "="*60)
    print("TESTING HTML PAGES")
    print("="*60)
    tester.test_html_pages()
    
    print("\n" + "="*60)
    print("TESTING STATIC ASSETS")
    print("="*60)
    tester.test_static_assets()
    
    # Print summary
    success = tester.print_summary()
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())