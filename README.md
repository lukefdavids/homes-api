# Nashville Homes — Backend

This is the backend of ***Nashville Homes***, a solo capstone project built as the culmination of six months of full-stack development training at [Nashville Software School](https://nashvillesoftwareschool.com/). It powers the frontend React app and handles data storage, authentication, and CRUD logic using Django and the Django REST Framework.

> 🔗 [Frontend Repository](https://github.com/lukefdavids/homes-client)
---

## Technologies Used

- Python 3.13.3
- Django
- Django REST Framework (DRF)
- SQLite3
- DRF Token Authentication

---

## Getting Started

### Prerequisites

- Python 3.13+
- Pip (comes with Python)
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:lukefdavids/homes-api.git
   cd nashville-homes-backend

2. Create and activate a virtual environment:
   
      ```bash
      python -m venv env
      source env/bin/activate

3. Install dependencies:

      ```bash
      pip install -r requirements.txt

4. Run migrations and seed database:

      ```bash
      ./seed_database.sh

5. Start the development server


