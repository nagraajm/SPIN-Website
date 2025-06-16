#!/bin/bash

# Script to update navigation in all HTML pages

# Define the new navigation HTML for pages in the pages/ directory
read -r -d '' NEW_NAV << 'EOF'
            <nav class="nav" role="navigation">
                <button class="nav-toggle" aria-label="Toggle navigation">
                    <span></span>
                    <span></span>
                    <span></span>
                </button>
                <ul class="nav-menu">
                    <li><a href="../index.html" class="nav-link">Home</a></li>
                    <li class="nav-item dropdown">
                        <a href="about.html" class="nav-link dropdown-toggle">About <i class="dropdown-arrow">▼</i></a>
                        <ul class="dropdown-menu">
                            <li><a href="about.html#presidents-welcome" class="dropdown-link">President's Welcome</a></li>
                            <li><a href="about.html#founding-members" class="dropdown-link">Founding Members</a></li>
                            <li><a href="about.html#executive-committee" class="dropdown-link">Executive Committee</a></li>
                            <li><a href="about.html#scientific-committee" class="dropdown-link">Scientific Committee</a></li>
                            <li><a href="about.html#research-admin-team" class="dropdown-link">Research and Admin Team</a></li>
                            <li><a href="about.html#rising-stars" class="dropdown-link">Rising Stars</a></li>
                        </ul>
                    </li>
                    <li><a href="membership.html" class="nav-link">Membership</a></li>
                    <li class="nav-item dropdown">
                        <a href="education.html" class="nav-link dropdown-toggle">Education <i class="dropdown-arrow">▼</i></a>
                        <ul class="dropdown-menu">
                            <li><a href="society-fellowship.html" class="dropdown-link">Society Fellowship</a></li>
                            <li><a href="education.html" class="dropdown-link">Education Offerings</a></li>
                            <li><a href="cortex-club.html" class="dropdown-link">Cortex Club</a></li>
                            <li><a href="spin-yarn-newsletter.html" class="dropdown-link">SPIN Yarn Newsletter</a></li>
                            <li><a href="spin-wfpi.html" class="dropdown-link">SPIN-WFPI</a></li>
                            <li><a href="spin-reporting-room.html" class="dropdown-link">SPIN Reporting Room</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="research.html" class="nav-link dropdown-toggle">Research <i class="dropdown-arrow">▼</i></a>
                        <ul class="dropdown-menu">
                            <li><a href="case-of-the-month.html" class="dropdown-link">Case of the Month Submission</a></li>
                            <li><a href="submit-proposal.html" class="dropdown-link">Submit a Proposal</a></li>
                            <li><a href="green-radiology.html" class="dropdown-link">Green Radiology</a></li>
                        </ul>
                    </li>
                    <li><a href="login.html" class="nav-link login-btn">Login</a></li>
                </ul>
            </nav>
EOF

echo "Navigation update script created successfully"
