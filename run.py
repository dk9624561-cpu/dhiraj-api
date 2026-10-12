import os
from api.index import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"\n[SERVER] StudyMate API Server running at: http://localhost:{port}")
    print(f" - Health Check: http://localhost:{port}/health")
    print(f" - Video API:    http://localhost:{port}/api/video/179326")
    print(f" - Lesson API:   http://localhost:{port}/api/lesson/4326")
    print(f" - Batches API:  http://localhost:{port}/api/batches\n")
    app.run(host='0.0.0.0', port=port, debug=False)

