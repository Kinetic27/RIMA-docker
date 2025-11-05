# 1. Base Image
FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-devel

# 2. Install system dependencies
RUN apt-get update && apt-get install -y git libarchive13 && \
    rm -rf /var/lib/apt/lists/*

# 3. Install Mamba
RUN conda install -n base -c conda-forge mamba -y

# 4. Set working directory
WORKDIR /workspace

# 5. Clone the repo (필요시 특정 브랜치/커밋 checkout)
RUN git clone https://github.com/Kinetic27/RIMA-docker.git . \
 && git submodule update --init --recursive || true

# 6. Create the conda environment
RUN mamba env create -f /workspace/environment.yml

# 7. Activate rima env for subsequent commands
SHELL ["conda", "run", "-n", "rima", "/bin/bash", "-c"]

# 8. Install local editable packages and extra pip deps
RUN pip install --no-cache-dir -e /workspace/perturbot/ && \
    pip install --no-cache-dir -e /workspace/ott-local/ && \
    pip install --no-cache-dir timm

# 9. Auto-activate rima whenever a shell starts
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc && \
    echo "conda activate rima" >> /root/.bashrc

# 10. Default command
CMD ["/bin/bash"]